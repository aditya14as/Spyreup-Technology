# Generated by Django 3.2.4 on 2021-06-17 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0009_plan_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('plan', models.CharField(max_length=200)),
                ('payment_id', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('user_id', models.IntegerField(null=True)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
