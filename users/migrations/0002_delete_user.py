# Generated by Django 4.1.7 on 2023-04-04 11:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]