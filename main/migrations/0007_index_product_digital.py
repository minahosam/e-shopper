# Generated by Django 3.2.3 on 2021-08-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210729_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='product_digital',
            field=models.BooleanField(default=True),
        ),
    ]
