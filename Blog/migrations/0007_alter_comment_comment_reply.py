# Generated by Django 3.2.3 on 2021-06-21 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_comment_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c_replied', to='Blog.comment'),
        ),
    ]