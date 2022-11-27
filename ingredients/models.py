from uuid import UUID, uuid4

from django.db import models
from django.utils.timezone import now

from .managers import IngredientManager


class Ingredient(models.Model):
    __unit_choices = (
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
        primary_key=True,
        max_length=36,
        unique=True,
        editable=False,
        default=uuid4(),
    )
    name = models.CharField(name="name", max_length=80, null=False, unique=True)
    vegetarian = models.BinaryField(name="vegetarian", default=False)
    calories = models.PostitveSmallIntegerField(
        name="calories", null=False, default=0, editable=True
    )
    fat = models.PositiveSmallIntegerField(name="fat", null=False, default=0, editable=True)
    protein = models.PositiveSmallIntegerField(
        name="protein", null=False, default=0, editable=True
    )
    units = models.CharField(
        name="units",
        choices=__unit_choices,
        max_length=3,
    )
    create_date = models.DateTimeField(name="create_date", editable=False, default=now)
    modify_date = models.DateTimeField(name="modify_date", default=now)

    objects = IngredientManager()

    def serialize(self) -> dict:
        return {
            "ingredient_id": self.ingredient_id,
            "name": self.name,
            "vegetarian": self.vegetarian,
            "calories": float(self.calories),
            "fat": float(self.fat),
            "protein": float(self.protein),
            "units": self.get_units_display(),
            "create_date": self.create_date,
            "modify_date": self.modify_date,
        }

    def __str__(self) -> str:
        return f"{self.name}({self.ingredient_id}) [Calories: {self.calories} Fat: {self.fat} Protein: {self.protein}]"
