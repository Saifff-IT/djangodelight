from django.urls import path, include
from . import views
urlpatterns = [
    path("inventory_list/", views.ListIngredients.as_view(), name="inventorylist"),
    path("menu_items/", views.ListMenuItem.as_view(), name="menuitems"),
    path("purchases/", views.ListPurchases.as_view(), name="purchases"),
    path("profit/", views.get_revenue_and_profit, name="profit"),
    path("delete_ingredient/<pk>",
         views.DeleteIngredient.as_view(), name="deleteingredient"),
    path("", views.home, name="home"),
    path("add_item", views.AddMenu.as_view(), name="addmenu"),
    path("add_ingredient", views.AddIngredient.as_view(), name="addingredient"),
    path("add_recipe", views.AddRecipeRequirement.as_view(), name="addrecipe"),
    path("add_purchase", views.AddPurchase.as_view(), name="addpurchase"),
    path("check", views.check, name="check"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.red, name="red")
]
