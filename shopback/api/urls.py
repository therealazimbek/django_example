from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('products/', views.productsPage),
    path('products/<int:pk>/', views.product_detailsPage),
    path('categories/', views.categoriesPage),
    path('categories/<int:pk>/', views.category_detailsPage),
    path('categories/<int:pk>/products/', views.category_products)
]
