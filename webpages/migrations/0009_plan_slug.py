# Generated by Django 3.2.4 on 2021-06-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0008_rename_sliderid_slider_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='slug',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
