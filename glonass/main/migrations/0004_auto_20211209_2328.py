# Generated by Django 3.2.9 on 2021-12-10 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211210_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preferences',
            old_name='blackHoles',
            new_name='high_magnitude',
        ),
        migrations.RenameField(
            model_name='preferences',
            old_name='galaxies',
            new_name='high_variability',
        ),
        migrations.RenameField(
            model_name='preferences',
            old_name='moons',
            new_name='low_variability',
        ),
        migrations.RenameField(
            model_name='preferences',
            old_name='planets',
            new_name='multi_star_system',
        ),
        migrations.RenameField(
            model_name='preferences',
            old_name='stars',
            new_name='survey_star',
        ),
    ]