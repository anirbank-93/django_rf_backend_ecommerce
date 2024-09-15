from django.urls import path

from .views import (
    CreateProductCategoryView,
    CreateProductView,
    GetProductsView
)

urlpatterns = [
    path('create-product-category/', CreateProductCategoryView.as_view(), name='create_product_category'),
    path('create-product/', CreateProductView.as_view(), name='create_product'),
    path('products/', GetProductsView.as_view(), name='product_list'),
]