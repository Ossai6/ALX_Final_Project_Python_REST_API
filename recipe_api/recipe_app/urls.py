# In recipe_app/urls.py
from django.urls import path
from .views import RecipeCreate, GetAllRecipes, GetSingleRecipe, RecipeDelete, RecipeUpdate, home
from recipe_app import views

urlpatterns = [
    path('recipe', views.home, name='home'),
    path('recipe/create', RecipeCreate.as_view(), name='recipe-create'),
    path('recipe/all/', GetAllRecipes.as_view(), name='get-all-recipes'),
    path('recipe/<int:id>/', GetSingleRecipe.as_view(), name='get-single-recipe'),
    path('recipe/delete/<int:id>/', RecipeDelete.as_view(), name='recipe-delete'),
    path('recipe/update/<int:id>/', RecipeUpdate.as_view(), name='recipe-update'),
]
