# Generated by Django 3.2.6 on 2021-12-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lodging', '0005_lodging_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date_publication',
            field=models.DateTimeField(null=True, verbose_name='дата публикации'),
        ),
    ]
