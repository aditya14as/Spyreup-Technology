# Generated by Django 3.2.4 on 2021-06-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='active',
            field=models.CharField(choices=[('active', 'active')], max_length=255, null=True),
        ),
    ]
