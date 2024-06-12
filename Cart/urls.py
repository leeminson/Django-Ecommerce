from django.urls import path
from . import views

urlpatterns = [
    path('Cart/', views.get_cart, name='Cart'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart')
]