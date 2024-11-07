from django.db.models import Avg
from django.shortcuts import render, Http404
from rest_framework import generics, response, status, permissions
from recipe_app.models import Recipe
from recipe_app.serializers import RecipeSerializer
from django.http import HttpResponse
from recipe_app import models


# Creating a recipe.
class RecipeCreate(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Recipe.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            recipe = serializer.save()
            return response.Response({
                "status": status.HTTP_200_OK,
                "response": f"{recipe.title} recipe created successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return response.Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "error": serializer.errors 
        }, status=status.HTTP_400_BAD_REQUEST)
    

# Retrieving all recipes
class GetAllRecipes(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        serializer = self.serializer_class(recipes, many=True)
        return response.Response({
            "status": status.HTTP_200_OK,
            "response": "Data retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        

# Retrieving a single recipe by ID
class GetSingleRecipe(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, *args, **kwargs):
        recipe_id = kwargs.get("id")
        recipe = Recipe.objects.filter(id=recipe_id).first()
        if recipe:
            serializer = self.serializer_class(recipe)
            return response.Response({
                "status": status.HTTP_200_OK,
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return response.Response({
            "status": status.HTTP_404_NOT_FOUND,
            "message": "Recipe with the specified ID does not exist"
        }, status=status.HTTP_404_NOT_FOUND)
            

# Deleting a recipe by ID
class RecipeDelete(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    
    def delete(self, request, *args, **kwargs):
        recipe_id = kwargs.get("id")
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            recipe.delete()
            return response.Response({
                "status": status.HTTP_202_ACCEPTED,
                "message": "Recipe deleted successfully"
            }, status=status.HTTP_202_ACCEPTED)
        except Recipe.DoesNotExist:
            raise Http404("Recipe not found")


# Updating a recipe by ID
class RecipeUpdate(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    
    def put(self, request, *args, **kwargs):
        recipe_id = kwargs.get("id")
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            serializer = self.serializer_class(recipe, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response({
                    "status": status.HTTP_202_ACCEPTED,
                    "message": "Recipe updated successfully",
                    "data": serializer.data
                }, status=status.HTTP_202_ACCEPTED)
            return response.Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Invalid data",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Recipe.DoesNotExist:
            raise Http404("Recipe not found")

    
    from rest_framework import generics, response, status
from recipe_app.models import Recipe
from recipe_app.serializers import RecipeSerializer
from django.db.models import Avg


import logging

logger = logging.getLogger(__name__)

class AdvancedSearch(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all().annotate(average_rating=Avg('ratings__rating'))
        
        # Filter by title
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        # Filter by ingredients
        ingredients = self.request.query_params.get('ingredients')
        if ingredients:
            ingredients_list = ingredients.split(',')
            logger.debug(f"Searching for ingredients: {ingredients_list}")
            queryset = queryset.filter(ingredients__name__in=ingredients_list).distinct()

        # Filter by cooking time
        cooking_time = self.request.query_params.get('cooking_time')
        if cooking_time:
            queryset = queryset.filter(cooking_time__lte=cooking_time)

        # Filter by difficulty level
        difficulty_level = self.request.query_params.get('difficulty_level')
        if difficulty_level:
            queryset = queryset.filter(difficulty_level=difficulty_level)

        logger.debug(f"Queryset after filtering: {queryset}")
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response({
            "status": status.HTTP_200_OK,
            "response": "Data retrieved successfully",
            "data": serializer.data
        })





from rest_framework import generics
from recipe_app.models import Rating
from recipe_app.serializers import RatingSerializer

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


from rest_framework import generics
from recipe_app.models import Rating
from recipe_app.serializers import RatingSerializer

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


from rest_framework import generics
from recipe_app.models import Rating
from recipe_app.serializers import RatingSerializer

class RecipeRatings(generics.ListCreateAPIView):
    """
    View to list all ratings for a specific recipe or create a new rating.
    """
    serializer_class = RatingSerializer

    def get_queryset(self):
        recipe_id = self.kwargs.get('recipe_id')
        return Rating.objects.filter(recipe_id=recipe_id)

    def perform_create(self, serializer):
        # Get the recipe from the URL parameter
        recipe_id = self.kwargs.get('recipe_id')
        # Get the currently authenticated user
        user = self.request.user if self.request.user.is_authenticated else None
        # Save the rating with both the user and the recipe
        serializer.save(recipe_id=recipe_id, user=user)


# Home page view
def home(request):
    return HttpResponse("Welcome to the Recipe API")
