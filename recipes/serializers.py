from rest_framework import serializers

from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "recipe_id",
            "recipe_name",
            "creator",
            "price",
            "meal_type",
            "description"
            "create_date",
            "modify_date",
        )