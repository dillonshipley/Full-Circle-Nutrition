# Generated by Django 4.1.1 on 2022-11-12 23:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_alter_recipe_recipe_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="recipe_id",
            field=models.UUIDField(
                default=uuid.UUID("c3b40618-1aa2-4bf0-96bc-25955e767275"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
