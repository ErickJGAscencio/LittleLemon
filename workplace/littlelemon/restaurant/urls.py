from django.urls import path, include
from rest_framework import routers
from .api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'menu', views.MenuItemsViewSet)
router.register(r'booking', views.BookingViewSet)

urlpatterns = [
  path('', include(router.urls)),
]