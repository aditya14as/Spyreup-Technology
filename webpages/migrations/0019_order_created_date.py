# Generated by Django 3.2.4 on 2021-06-19 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0018_rename_development_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]