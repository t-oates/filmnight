from django.shortcuts import render
import random

from .models import Night, Film, Voter, Vote


def index(request):
    return vote_page(request)


def vote_page(request):
    current_night = Night.objects.filter(state='voting').first()

    voting_options = range(6)

    context = {
        "voting_options": voting_options,
        "voted": False
    }

    if request.method == 'POST':
        data = request.POST

        film_ids = [int(film_id.strip())
                    for film_id in data['film_order'].split()]
        context['films'] = [Film.objects.get(id=film_id)
                            for film_id in film_ids]

        context['voted'] = True
        context['voter_name'] = data['name']

        voter = Voter.objects.create(name=data['name'],
                                     film_night=current_night)

        for film in context['films']:
            if f'film_{film.id}_score' in data:
                score = int(data[f'film_{film.id}_score'])
                Vote.objects.create(voter=voter, film=film, score=score)
                film.score = score
    else:
        films = Film.objects.filter(nights=current_night)
        context['films'] = random.sample(list(films), len(films))

    return render(request, 'polls/vote.html', context)


def results(request):
    current_night = Night.objects.filter(state='voting').first()
    films = Film.objects.filter(nights=current_night)
    voters = Voter.objects.filter(film_night=current_night)
    votes = Vote.objects.filter(voter__film_night=current_night)

    for film in films:
        film_votes = votes.filter(film=film)
        film.total = sum(vote.score for vote in film_votes)

    films = sorted(films, key=lambda x: x.total, reverse=True)

    context = {
        'films': films,
        'voters': voters,
        'votes': votes
    }

    return render(request, 'polls/results.html', context)
