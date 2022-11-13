# Generated by Django 4.1.1 on 2022-11-12 23:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0003_alter_recipe_recipe_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="recipe_id",
            field=models.UUIDField(
                default=uuid.UUID("8511bf0f-afa8-45f9-8adc-cd5482639ea8"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
