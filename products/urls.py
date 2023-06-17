from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('all', AllProductsView, basename='all-products')
router.register('category/(?P<category>\w+)', CategoryView, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
