# Generated by Django 3.2.6 on 2021-10-28 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='name')),
                ('surname', models.CharField(blank=True, max_length=100, verbose_name='surname')),
                ('birthday', models.DateField(blank=True, verbose_name='birthday')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='title')),
                ('isbn', models.CharField(blank=True, max_length=100, verbose_name='isbn')),
                ('release', models.DateField(blank=True, verbose_name='release')),
                ('pages', models.CharField(blank=True, max_length=100, verbose_name='pages')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_goods.author')),
            ],
        ),
    ]
