# Generated by Django 3.2.3 on 2021-05-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='post',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]