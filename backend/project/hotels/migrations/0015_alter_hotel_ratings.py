# Generated by Django 5.0 on 2024-01-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0014_alter_hotel_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='ratings',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
    ]
