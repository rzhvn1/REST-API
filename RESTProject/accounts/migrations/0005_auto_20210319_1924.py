# Generated by Django 3.1.7 on 2021-03-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='date',
            field=models.DateField(),
        ),
    ]
