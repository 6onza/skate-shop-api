from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('all', AllProductsView, basename='all-products')
router.register('category/(?P<category>\w+)', CategoryView, basename='category')
router.register('sorted/desc', AllProductsViewDescByPrice, basename='all-products-desc')
router.register('sorted/asc', AllProductsViewAscByPrice, basename='all-products-asc')

urlpatterns = [
    path('', include(router.urls)),
]
