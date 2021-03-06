# Generated by Django 2.2.9 on 2020-01-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_test"),
        ("users", "0002_auto_20200123_1017"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tester",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tester",
                    models.ManyToManyField(
                        related_name="tester_tester", to="home.CustomText"
                    ),
                ),
                (
                    "tt",
                    models.ManyToManyField(
                        related_name="tester_tt", to="home.HomePage"
                    ),
                ),
            ],
        ),
    ]
