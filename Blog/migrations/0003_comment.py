# Generated by Django 3.2.3 on 2021-06-15 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0002_auto_20210613_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_email', models.EmailField(max_length=100)),
                ('current_city', models.CharField(max_length=50)),
                ('comment_content', models.TextField(max_length=300)),
                ('comment_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('comment_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Blog.blog')),
            ],
            options={
                'ordering': ['comment_blog'],
            },
        ),
    ]
