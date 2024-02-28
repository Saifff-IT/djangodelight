from django.contrib import admin
from .models import MenuItem, Ingredient, Purchase, RecipeRequirement

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Purchase)
admin.site.register(RecipeRequirement)