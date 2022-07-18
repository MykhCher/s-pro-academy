from django.db import models


class Store(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Name'
    )
    description = models.CharField(
        max_length=800,
        verbose_name='Description'
    )
    rating = models.IntegerField(
        verbose_name='Rating'
    )
