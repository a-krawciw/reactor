# pylint: disable=no-member, unsubscriptable-object

from django.db import models
from django.urls import reverse
from django.utils import timezone

from discordbot.botmodules.bots import VierGewinntBot
from discordbot.botmodules.parser import HTMLCleaner

from discordbot.config import DOMAIN

from asgiref.sync import sync_to_async

import time
import uuid
import re


class ReactionMapping(models.Model):
    user = models.CharField(max_length=200)
    reaction = models.CharField(max_length=200)
    guild_id = models.IntegerField()

    def get_emoji(self):
        return f"\\{self.reaction}"

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.user}->{self.reaction}"