# Generated by Django 4.1.5 on 2023-05-29 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_booking_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking_detail',
            old_name='drop_date',
            new_name='drop_time',
        ),
    ]
