from django.db import models

# Create your models here.


class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Movie(models.Model):
    network = models.ForeignKey(Network, related_name="network", on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.TextField(default="")
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)