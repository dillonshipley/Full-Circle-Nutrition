import uuid

from django.db import models
from django.utils.timezone import now


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
		default=uuid.uuid4(),
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
