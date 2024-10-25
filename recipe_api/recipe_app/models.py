from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    instructions = models.TextField(max_length=500, null=True, blank=True)
    cooking_time = models.CharField(max_length=500, null=True, blank=True)
    difficulty_level = models.CharField(max_length=500, null=True, blank=True)
    source = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"