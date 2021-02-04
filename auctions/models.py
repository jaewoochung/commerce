from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


# add Classes for auction listings, bids, comments, auction categories
"""
Models: Your application should have at least three models in addition to the User model: one for
auction listings, one for bids, and one for comments made on auction listings. It’s up to you to
decide what fields each model should have, and what the types of those fields should be.
You may have additional models if you would like.
"""
# Each time you add a class or change models.py
# python manage.py makemigrations
# python manage.py migrate


class Listing(models.Model):
    # Need to make a relation to user
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=120)
    bid = models.IntegerField()
    image = models.CharField(max_length=200)
    num_bids = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bidder = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.id}: {self.title} to {self.description}"
