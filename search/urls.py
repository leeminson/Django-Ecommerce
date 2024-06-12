from django.urls import path

from search import views

urlpatterns = (
 path('results/', views.results, name='search_results'),
 
)