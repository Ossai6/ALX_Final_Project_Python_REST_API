from django.shortcuts import render, Http404
from rest_framework import generics, response, status, permissions
from recipe_app.models import Recipe
from recipe_app.serializers import RecipeSerializer
from django.http import HttpResponse


# Creating a recipe.
class RecipeCreate(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Recipe.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
                "status": status.HTTP_200_OK,
                "response": "Data posted successfully",
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

# Home page view
def home(request):
    return HttpResponse("Welcome to the Recipe API")
