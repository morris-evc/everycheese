from enum import unique
from django.db import models

# Create your models here.
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

class Cheese(TimeStampedModel):

    class Firmness(models.TextChoices):
        #enum-powered choices
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"
    
    firmness = models.CharField("Firmness", max_length=20,
        choices=Firmness.choices, default=Firmness.UNSPECIFIED)

    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address",
    unique=True, always_update=False, populate_from="name")

    description = models.TextField("Description", blank=True)

    def __str__(self):
        return self.name

