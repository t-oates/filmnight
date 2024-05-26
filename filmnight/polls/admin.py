from django.contrib import admin

# Register your models here.
from .models import Night, Voter, Film, Vote

admin.site.register(Night)
admin.site.register(Voter)
admin.site.register(Film)
admin.site.register(Vote)
