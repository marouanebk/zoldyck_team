# Generated by Django 4.0.4 on 2022-05-27 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
