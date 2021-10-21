# Generated by Django 3.2.6 on 2021-09-23 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0015_alter_news_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('description', models.TextField(blank=True)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('news', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file', to='app_news.news')),
            ],
        ),
    ]