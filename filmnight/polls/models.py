from django.db import models


class Night(models.Model):
    date = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.date} ({self.state})'


class Voter(models.Model):
    name = models.CharField(max_length=200)
    film_night = models.ForeignKey(Night, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=200)
    nights = models.ManyToManyField(Night)

    def __str__(self):
        return self.name


class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.film.name}: {self.score}'
