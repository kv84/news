# Generated by Django 3.2.6 on 2021-11-13 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0009_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_market.product')),
            ],
        ),
    ]
