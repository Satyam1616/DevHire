# Generated by Django 5.1.4 on 2025-01-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_meetingrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingrequest',
            name='meeting_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='meetingrequest',
            name='room_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
