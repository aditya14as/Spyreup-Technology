# Generated by Django 3.2.4 on 2021-06-18 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0012_auto_20210617_1352'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Checkout',
        ),
    ]
