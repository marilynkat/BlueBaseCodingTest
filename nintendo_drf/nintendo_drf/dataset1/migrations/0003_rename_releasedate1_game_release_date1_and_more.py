# Generated by Django 4.0.8 on 2022-11-26 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataset1', '0002_rename_gameset1_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='releaseDate1',
            new_name='release_date1',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='releaseDate2',
            new_name='release_date2',
        ),
    ]