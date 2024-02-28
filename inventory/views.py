from datetime import datetime
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView
from django.contrib import messages
from inventory.forms import *
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ListIngredients(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/inventory_list.html"
    context_object_name = "ingredients"


class DeleteIngredient(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = reverse_lazy("inventorylist")


class ListMenuItem(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu_items.html"
    context_object_name = "items"


class ListPurchases(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchases.html"
    context_object_name = "purchases"


@login_required
def get_revenue_and_profit(request):
    purchases = Purchase.objects.all()
    revenue = 0
    profit = 0
    cost = 0
    for purchase in purchases:
        revenue += purchase.menu_item.price
        requirements = RecipeRequirement.objects.filter(
            menu_item=purchase.menu_item)
        for require in requirements:
            cost += require.ingredient.unit_price * require.quantity
        profit += revenue - cost
    context = {"revenue": revenue, "profit": profit,
               "date": datetime.today().date(), "cost": cost}
    return render(request, "inventory/profit.html", context)


def home(req):
    items = MenuItem.objects.all()
    context = {"items": items, "user": req.user}
    return render(req, "inventory/home.html", context)


def red(req):
    return redirect("/")


class AddMenu(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/add_menu.html"
    success_url = reverse_lazy("menuitems")
    form_class = MenuItemForm


class AddIngredient(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    success_url = reverse_lazy("inventorylist")
    form_class = IngredientForm


class AddRecipeRequirement(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/add_recipe.html"
    success_url = reverse_lazy("home")
    form_class = RecipeRequirementForm


class AddPurchase(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/add_purchase.html"
    form_class = PurchaseForm


@login_required
def check(request):
    flag = True
    if request.method == "POST":
        print(request.POST)
        item = request.POST["menu_item"]
        recipe = RecipeRequirement.objects.filter(menu_item=item)
        for r in recipe:
            if r.quantity > r.ingredient.quantity:
                flag = False
                break
        if flag:
            for r in RecipeRequirement.objects.filter(menu_item=request.POST["menu_item"]):
                r.ingredient.quantity -= r.quantity
                r.ingredient.save()
            p = Purchase(menu_item=MenuItem.objects.get(
                id=request.POST["menu_item"]))
            p.save()
        else:
            messages.error(request, "Cannot Purchase, lack of ingredients!")
            return redirect("/add_purchase")
        return redirect("/purchases")
