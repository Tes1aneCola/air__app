from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register(r'Users',UserViewSet , basename='user')
router.register(r'properties',PropertyListViewSet , basename='property')
router.register(r'bookings',BookingViewSet , basename='booking')
router.register(r'reviews',ReviewViewSet , basename='review')
router.register(r'amenity',AmenityViewSet , basename='amenity')

urlpatterns = [path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),]