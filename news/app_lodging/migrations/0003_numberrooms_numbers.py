# Generated by Django 3.2.6 on 2021-11-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lodging', '0002_rename_lodgigng_type_lodging_lodging_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='numberrooms',
            name='numbers',
            field=models.CharField(blank=True, max_length=100, verbose_name='количество'),
        ),
    ]
