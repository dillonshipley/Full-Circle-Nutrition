from rest_framework import serializers

from .models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            "ingredient_id",
            "name",
            "vegetarian",
            "calories",
            "fat",
            "protein",
            "units",
            "create_date",
            "modify_date",
        )
