from django import forms
from .models import *


class MenuItemForm(forms.ModelForm):
    class Meta:
        fields = ["title", "price"]
        model = MenuItem


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["menu_item"]
