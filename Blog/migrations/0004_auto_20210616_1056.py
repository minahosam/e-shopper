# Generated by Django 3.2.3 on 2021-06-16 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
