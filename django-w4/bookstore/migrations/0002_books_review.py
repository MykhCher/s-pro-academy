# Generated by Django 4.0.5 on 2022-07-17 13:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='review',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
