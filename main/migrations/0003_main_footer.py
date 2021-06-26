# Generated by Django 3.2.3 on 2021-06-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='main_footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone_number', models.IntegerField(default=0)),
                ('e_mail', models.EmailField(max_length=20)),
                ('facebook_link', models.CharField(max_length=20)),
                ('twitter_link', models.CharField(max_length=20)),
                ('linkedin_link', models.CharField(max_length=20)),
                ('google_link', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
            ],
        ),
    ]
