# Generated by Django 3.2.8 on 2021-10-29 04:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ticket", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="reviewed",
        ),
    ]
