# Generated by Django 3.1.7 on 2021-03-24 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_remove_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealtoorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MTO', to='order.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Ready', 'Ready'), ('In process', 'In process'), ('Closed', 'Closed')], default='In process', max_length=20),
        ),
    ]
