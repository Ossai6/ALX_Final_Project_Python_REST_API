from rest_framework import serializers
from recipe_app.models import Recipe, Rating, Ingredient

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = ['id', 'recipe', 'user', 'rating', 'review', 'created_at']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    ingredients = IngredientSerializer(many=True, required=False)  # Use IngredientSerializer for ingredients

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'instructions', 'cooking_time', 
                  'difficulty_level', 'date_created', 'author', 'ingredients', 
                  'ratings', 'average_rating']

    def create(self, validated_data):
        # Extract the list of ingredients from validated_data, or use an empty list if not provided
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)

        # Add each ingredient to the recipe, creating it if necessary
        for ingredient_data in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient_data['name'])
            recipe.ingredients.add(ingredient)

        return recipe

    def update(self, instance, validated_data):
        # Extract the list of ingredients from validated_data, or use an empty list if not provided
        ingredients_data = validated_data.pop('ingredients', [])
        
        # Update other fields on the instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update the ingredients if ingredients_data is provided
        if ingredients_data:
            instance.ingredients.clear()  # Clear existing ingredients
            for ingredient_data in ingredients_data:
                ingredient, created = Ingredient.objects.get_or_create(name=ingredient_data['name'])
                instance.ingredients.add(ingredient)

        return instance
