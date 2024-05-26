from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="vote"),
    path("results", views.results, name="results")
]
