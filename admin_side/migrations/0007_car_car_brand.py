# Generated by Django 4.1.5 on 2023-05-16 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0006_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_brand',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='admin_side.brand'),
            preserve_default=False,
        ),
    ]
