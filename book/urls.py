from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('product/', views.list_product, name="product"),
    path('product/<slug>/', views.product_detail, name="product-detail"),
]