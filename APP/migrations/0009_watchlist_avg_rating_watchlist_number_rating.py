# Generated by Django 4.1.4 on 2022-12-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0008_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
