# Generated by Django 3.1.7 on 2021-03-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_meal_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
