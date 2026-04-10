from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('product/<int:id>/', views.product_detail),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
]
