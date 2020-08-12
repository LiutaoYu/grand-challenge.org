# Generated by Django 2.1.5 on 2019-02-04 15:17

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("cases", "0008_auto_20190201_1312")]

    operations = [
        migrations.CreateModel(
            name="Archive",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        default="Unnamed Archive", max_length=255
                    ),
                ),
                ("images", models.ManyToManyField(to="cases.Image")),
            ],
            options={"abstract": False},
        )
    ]