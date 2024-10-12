
from django.urls import path,include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'catalogs', CatalogViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    
]