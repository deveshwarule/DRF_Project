# Generated by Django 4.1.3 on 2022-12-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_streamplatform_watchlist_delete_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
