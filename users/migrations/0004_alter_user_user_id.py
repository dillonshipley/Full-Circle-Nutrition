# Generated by Django 4.1.1 on 2022-11-12 23:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.UUIDField(
                default=uuid.UUID("9027d1a3-df52-4c2c-b08b-b1d6ba9c4f25"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
