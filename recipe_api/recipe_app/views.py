from django.shortcuts import render, Http404
from rest_framework import generics, response, status, permissions
from recipe_app.models import Recipe
from recipe_app.serializers import RecipeSerializer

# Creating a recipe.
class RecipeCreate(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Recipe.objects.all()
    
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response({
                    "status":status.HTTP_200_OK,
                    "response":"Data posted successfully",
                    "data":serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return response.Response({
                    "status":status.HTTP_400_BAD_REQUEST,
                    "error":serializer.errors 
                }, status=status.HTTP_400_BAD_REQUEST)
    
class GetAllRecipes(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get(self, *args, **kwargs):
        recipe = Recipe.objects.all()
        serializer = self.serializer_class(recipe, many=True)
        return response.Response({
            "status":status.HTTP_200_OK,
                    "response":"Data posted successfully",
                    "data":serializer.data
        }, status.HTTP_200_OK)
        
        
class GetSingleRecipe(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get(self, *args, **kwargs):
        recipe_id = kwargs.get("id")
        recipe = Recipe.objects.filter(id=recipe_id)
        if recipe:
            serializer = self.serializer_class(recipe, many=True)
            return response.Response({
                "status":status.HTTP_200_OK,
                "data":serializer.data
            }, status.HTTP_200_OK)
        else:
            return response.Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Sorry, recipe with the above id does not exists"
            }, status.HTTP_400_BAD_REQUEST)
            
class RecipeDelete(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    
    @staticmethod
    def get_recipe_object(self, id, *args, **kwargs):
        try:
            return Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            raise Http404
        
    def delete(self, id, request, *args, **kwargs):
        recipe = self.get_recipe_object(id)
        recipe.delete(id)
        return response.Response({
            "status":status.HTTP_202_ACCEPTED,
            "message":"Recipe deleted successfully"
        })