from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/', views.products, name='products'),

    # Product Details Page
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path(
    'wishlist/<int:product_id>/',
    views.add_to_wishlist,
    name='add_to_wishlist'
),
    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
]