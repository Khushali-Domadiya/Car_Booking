# Generated by Django 4.1.5 on 2023-05-16 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0009_alter_car_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='prize',
            field=models.BigIntegerField(),
        ),
    ]
