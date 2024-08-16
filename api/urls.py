from . import views
from django.urls import path

urlpatterns = [
    path("category/list", views.CategoryListView.as_view()),
    path("category/detail/<int:id>/", views.CategoryDetailView.as_view()),
    path("product/list", views.ProductListView.as_view()),
    path("category/detail/<int:id>/", views.ProductDetailView.as_view()),
]
