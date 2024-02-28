from django.db import models
from django.utils import timezone
# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField()

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.title


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self) -> str:
        return f"{self.menu_item}"


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.menu_item}"
