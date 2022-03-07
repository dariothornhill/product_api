from django.urls import path
from .views import ProductDelete, ProductListCreate, OrderListCreate

urlpatterns = [
    path("products/", ProductListCreate.as_view()),
    path("orders/", OrderListCreate.as_view()),
    path("products/<int:pk>/", ProductDelete.as_view()),
]