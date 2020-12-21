from django.db import models


class ReactionMapping(models.Model):
    user = models.CharField(max_length=200)
    reaction = models.CharField(max_length=200)
    guild_id = models.IntegerField()

