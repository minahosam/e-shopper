# Generated by Django 3.2.3 on 2021-06-23 09:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_index_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='add_to_cart',
            field=models.ManyToManyField(null=True, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='index',
            name='add_to_compare',
            field=models.ManyToManyField(null=True, related_name='compare', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='index',
            name='add_to_wishlist',
            field=models.ManyToManyField(null=True, related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]