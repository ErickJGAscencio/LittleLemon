from django.urls import path, include
from rest_framework import routers
from .api import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'menu', views.MenuViewSet)
# router.register(r'tables', views.BookingViewSet)
# router.register(r'menu-items', views.MenuItemsViewSet)
# router.register(r'menu-items/', views.SingleMenuItemView)

# RECORDAR CAMBIAR LAS RUTAS MANUALMENTE Y EN LOS ARCHIVOS VIEWS, CAMBIAR LA PROPIEDAD QUE HEREDAN
urlpatterns = [
  path('', include(router.urls)),
  path('', views.index, name='index'),
  path('booking/', include(router.urls)),
  path('message/', views.msg),
  path('api-token-auth/', obtain_auth_token),

  path('menu/', views.MenuViewSet.as_view()),
  path('menu-items/', views.MenuItemsView.as_view()),
  path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
  path('tables/', views.BookingViewSet.as_view()),
]