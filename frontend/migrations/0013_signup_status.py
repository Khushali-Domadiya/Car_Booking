# Generated by Django 4.1.5 on 2023-06-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_review_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
