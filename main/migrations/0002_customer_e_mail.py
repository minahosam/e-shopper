# Generated by Django 3.2.3 on 2021-07-06 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_alter_userprofile_email'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='e_mail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='customer_email', to='Profile.userprofile', to_field='email'),
            preserve_default=False,
        ),
    ]
