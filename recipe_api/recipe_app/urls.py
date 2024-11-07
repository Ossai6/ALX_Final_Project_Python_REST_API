from django.urls import path
from .views import RecipeCreate, GetAllRecipes, GetSingleRecipe, RecipeDelete, RecipeUpdate, AdvancedSearch, RatingList, RatingDetail, RecipeRatings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


# Initialize the schema view
schema_view = get_schema_view(
   openapi.Info(
      title="RECIPE FINDER API",
      default_version='v1',
      description="The Recipe Finder API provides a comprehensive platform for users to search, find, retrieve, update, and delete recipes. Additionally, users can rate and review recipes, and perform searches based on various filters.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="akpec116.com"),
      license=openapi.License(name="License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# URL patterns
urlpatterns = [
    # Your other app URLs
    path('recipe/', RecipeCreate.as_view(), name='recipe-create'),
    path('recipe/all/', GetAllRecipes.as_view(), name='get-all-recipes'),
    path('recipe/<int:id>/', GetSingleRecipe.as_view(), name='get-single-recipe'),
    path('recipe/delete/<int:id>/', RecipeDelete.as_view(), name='recipe-delete'),
    path('recipe/update/<int:id>/', RecipeUpdate.as_view(), name='recipe-update'),
    path('search/', AdvancedSearch.as_view(), name='advanced-search'),
    path('ratings/', RatingList.as_view(), name='rating-list'),
    path('ratings/<int:pk>/', RatingDetail.as_view(), name='rating-detail'),
    path('recipe/<int:recipe_id>/ratings/', RecipeRatings.as_view(), name='recipe-ratings'),

    # Swagger UI URL for your API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]