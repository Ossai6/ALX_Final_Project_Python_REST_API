from django.urls import path
from recipe_app.views import RecipeCreate, GetAllRecipes, RecipeDelete, GetSingleRecipe

urlpatterns = [
    path("create/", RecipeCreate.as_view(), name="create_recipe"),
    path("get_all_recipes/", RecipeCreate.as_view(), name="get_all_recipes"),
    path("get/<int:id>", GetSingleRecipe.as_view(), name="get_single_recipe"),
    path("delete/<int:id>", RecipeDelete.as_view(), name="recipe_delete"),
]
