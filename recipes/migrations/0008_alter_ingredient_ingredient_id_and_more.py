# Generated by Django 4.1.1 on 2022-10-06 02:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0007_alter_ingredient_ingredient_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="ingredient_id",
            field=models.UUIDField(
                default=uuid.UUID("92eb5e34-b7db-4f0d-a8e4-d92face9d419"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="recipe_id",
            field=models.UUIDField(
                default=uuid.UUID("187af72a-3b96-46a4-b76f-4a6199c102ee"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.UUIDField(
                default=uuid.UUID("b1e647b6-091c-414c-a70c-961b5b32efde"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
