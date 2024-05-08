from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.index, name="home"),
    path("shop", views.shop, name="shop"),
    path("products", views.products, name="products"),
    path("personal", views.personal, name="personal"),
    path("imprint", views.imprint, name="imprint"),
]