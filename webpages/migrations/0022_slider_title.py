# Generated by Django 3.2.4 on 2021-07-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0021_auto_20210706_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(choices=[('slider1', 'slider1'), ('slider2', 'slider2'), ('slider3', 'slider3')], default=True, max_length=50),
        ),
    ]