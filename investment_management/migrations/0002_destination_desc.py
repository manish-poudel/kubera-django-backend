# Generated by Django 5.0.7 on 2024-07-21 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
