# Generated by Django 4.1.7 on 2023-04-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("followers", "0002_alter_userfollows_options"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="userfollows",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="userfollows",
            constraint=models.UniqueConstraint(
                fields=("user", "followed_user"), name="unique_userfollows"
            ),
        ),
    ]
