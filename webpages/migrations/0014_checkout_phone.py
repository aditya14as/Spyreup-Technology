# Generated by Django 3.2.4 on 2021-06-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0013_rename_order_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='phone',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
