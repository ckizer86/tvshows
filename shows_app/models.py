from django.db import models
from time import gmtime, localtime, strftime
from datetime import date

# Create your models here.


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        today = str(date.today())
        movie_id = postData["movie_id"]
        this_movie = Movie.objects.get(id=movie_id)
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        for movie in Movie.objects.exclude(id=this_movie.id):
            if postData['title'] == movie.title:
                errors["title"] = "Title already exists"
        if len(postData['description']) != 0 and len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        if postData['release_date'] == "":
            errors["release_date"] = "Must have a release date"
        if postData['release_date'] > today:
            errors["release_date"] = "Date must be in the past"
        if postData['network'] == "none":
            errors["network"] = "Must select a network"
        return errors

    def new_validator(self, postData):
        today = str(date.today())
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        for movie in Movie.objects.all():
            if postData['title'] == movie.title:
                errors["title"] = "Title already exists"
        if len(postData['description']) != 0 and len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        if postData['release_date'] == "":
            errors["release_date"] = "Must have a release date"
        if postData['release_date'] > today:
            errors["release_date"] = "Date must be in the past"
        if postData['network'] == "none":
            errors["network"] = "Must select a network"
        return errors

class NetworkManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['add_network']) < 3:
            errors["add_network"] = "Network should be at least 3 characters"
        return errors


class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = NetworkManager()

class Movie(models.Model):
    network = models.ForeignKey(Network, related_name="network", on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.TextField(default="")
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()