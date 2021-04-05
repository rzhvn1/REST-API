# Generated by Django 3.1.7 on 2021-03-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='desc',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='meal',
            name='portion',
            field=models.CharField(choices=[('0.7', '0.7'), ('1', '1')], max_length=50),
        ),
    ]