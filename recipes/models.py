from django.db import models
from django.utils.timezone import now


class Recipe(models.Model):
    type_choices = (
        ("BF", "Breakfast"),
        ("SK", "Snack"),
        ("SM", "Standard Meal"),
    )

    recipe_id = models.UUIDField(
        name="recipe_id",
        primary_key=True,
        max_length=36,
        null=False,
        unique=True,
        editable=False,
        default="10000000-0000-0000-0000-000000000000",
    )
    name = models.CharField(name="name", max_length=80, null=False, unique=True)
    creator = models.CharField(name="creator", max_length=80, null=True)
    price = models.DecimalField(
        name="price", decimal_places=2, max_digits=10, default=0.00
    )
    recipe_type = models.CharField(
        name="recipe_type", choices=type_choices, max_length=2, null=True
    )
    description = models.CharField(name="description", max_length=500, null=True)
    create_date = models.DateTimeField(name="create_date", default=now)
    modify_date = models.DateTimeField(name="modify_date", default=now)


class Ingredient(models.Model):
    UNIT_CHOICES = (
        ("CUP", "cups"),
        ("TBP", "table spoon"),
        ("TSP", "tea spoon"),
        ("DSH", "dash"),
        ("PCH", "pinch"),
        ("LBS", "pound"),
        ("OZS", "ounce"),
        ("GRM", "gram"),
        ("SLC", "slice"),
    )

    ingredient_id = models.UUIDField(
        name="ingredient_id",
        max_length=36,
        null=False,
        primary_key=True,
        unique=True,
        editable=False,
        default="10000000-0000-0000-0000-000000000000",
    )
    name = models.CharField(name="name", max_length=80, null=False, unique=True)
    vegetarian = models.BinaryField(name="vegetarian", default=False)
    calories = models.SmallIntegerField(name="calories")
    fat = models.SmallIntegerField(name="fat")
    protein = models.SmallIntegerField(name="protein")
    units = models.CharField(
        name="units",
        choices=UNIT_CHOICES,
        max_length=3,
    )
    amount = models.DecimalField(name="", decimal_places=2, max_digits=8)
    create_date = models.DateTimeField(name="create_date", default=now)
    modify_date = models.DateTimeField(name="modify_date", default=now)


class UserManager(models.Manager):
    def user_count(self, keyword) -> int:
        return self.filter(user_id_icontain=keyword).count()


class User(models.Model):
    goal_choices = (
        ("-3", "Very rapid loss"),
        ("-2", "Rapid loss"),
        ("-1", "Moderate loss"),
        ("0", "Maintain"),
        ("1", "Moderate gain"),
        ("2", "Rapid gain"),
        ("3", "Very rapid gain"),
    )

    user_id = models.UUIDField(
        name="user_id",
        max_length=36,
        primary_key=True,
        null=False,
        unique=True,
        editable=False,
        default="10000000-0000-0000-0000-000000000000",
    )
    user_name = models.CharField(name="user_name", max_length=25, unique=True)
    age = models.IntegerField(name="age", null=False, default=25)
    height = models.DecimalField(
        name="height", decimal_places=2, null=False, max_digits=8, default=0.00
    )
    weight = models.DecimalField(
        name="weight", decimal_places=2, null=False, max_digits=8, default=0.00
    )
    body_fat = models.DecimalField(
        name="body_fat", decimal_places=2, null=False, max_digits=8, default=0.00
    )
    goal = models.CharField(
        name="goal", choices=goal_choices, max_length=2, null=False, default="0"
    )
    create_date = models.DateTimeField(name="create_date", default=now)
    modify_date = models.DateTimeField(name="modify_date", default=now)

    objects = UserManager()

    def __str__(self) -> str:
        return f"User({self.user_name}): {self.user_id}"
