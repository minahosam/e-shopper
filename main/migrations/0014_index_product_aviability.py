# Generated by Django 3.2.3 on 2021-06-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_index_transaction_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='product_aviability',
            field=models.CharField(choices=[('In Stock', 'In Stock'), ('Out Of Stock', 'Out Of Stock')], default='In Stock', max_length=17),
        ),
    ]