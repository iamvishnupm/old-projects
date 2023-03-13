from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("search/", views.search, name="search"),
    path("cart/", views.cart, name="cart"),
    path("cart/<int:id>", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:id>", views.remove_from_cart, name="remove_from_cart"),
    path("cart/delete/<int:id>", views.delete_item, name="delete_item"),
    path("<slug:c_slug>", views.home, name="c_home"),
    path("<slug:c_slug>/<slug:p_slug>", views.details, name="details"),
]