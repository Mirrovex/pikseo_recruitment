# Generated by Django 5.0.6 on 2024-05-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Wiek'),
        ),
    ]
