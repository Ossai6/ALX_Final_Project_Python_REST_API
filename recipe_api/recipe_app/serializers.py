from rest_framework import serializers
from recipe_app.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = "__al__"