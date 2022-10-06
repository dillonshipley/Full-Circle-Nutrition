import uuid

from django.db import models
from django.utils.timezone import now


class RecipeManager(models.Manager):
	def recipe_count(self, keyword) -> int:
		return self.filter(user_id_icontain=keyword).count()


class Recipe(models.Model):
	recipe_category_options = (
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
		default=uuid.uuid4(),
	)
	name = models.CharField(name="name", max_length=80, null=False, unique=True)
	creator = models.CharField(name="creator", max_length=80, null=True)
	price = models.DecimalField(
		name="price", decimal_places=2, max_digits=10, default=0.00
	)
	recipe_category = models.CharField(
		name="recipe_type", choices=recipe_category_options, max_length=2, null=True
	)
	description = models.CharField(name="description", max_length=500, null=True)
	create_date = models.DateTimeField(name="create_date", default=now)
	modify_date = models.DateTimeField(name="modify_date", default=now)
