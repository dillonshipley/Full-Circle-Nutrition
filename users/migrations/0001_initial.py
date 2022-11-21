# Generated by Django 4.1.1 on 2022-10-06 03:37

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "user_id",
                    models.UUIDField(
                        default=uuid.UUID("8ffaa4c5-3d7d-46a6-bac0-8402763cfb80"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("user_name", models.CharField(max_length=25, unique=True)),
                ("age", models.IntegerField(default=25)),
                (
                    "height",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                (
                    "weight",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                (
                    "body_fat",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                (
                    "goal",
                    models.CharField(
                        choices=[
                            ("-3", "Very rapid loss"),
                            ("-2", "Rapid loss"),
                            ("-1", "Moderate loss"),
                            ("0", "Maintain"),
                            ("1", "Moderate gain"),
                            ("2", "Rapid gain"),
                            ("3", "Very rapid gain"),
                        ],
                        default="0",
                        max_length=2,
                    ),
                ),
                (
                    "create_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "modify_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
