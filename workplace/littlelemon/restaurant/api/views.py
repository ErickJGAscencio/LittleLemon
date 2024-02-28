from rest_framework import viewsets
from rest_framework import generics
from .serializers import MenuSerializer, MenuItemSerializer, UserSerializer, BookingSerializer
from django.contrib.auth.models import User
from .models import Menu, MenuItem, Booking
from rest_framework import response
# from rest_framework import status
from rest_framework import permissions, authentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes

@api_view()
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.TokenAuthentication])
def msg(request):
  return response({"message":"This view is protected"})

class UserViewSet(viewsets.ModelViewSet):
  # permission_classes = [permissions.IsAuthenticated] 
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
class MenuViewSet(generics.ListCreateAPIView):
# class MenuViewSet(viewsets.ModelViewSet):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class MenuItemsView(generics.ListCreateAPIView):
# class MenuItemsViewSet(viewsets.ModelViewSet):
  # permission_classes = [permissions.IsAuthenticated]
  queryset = Menu.objects.all()
  serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.ListCreateAPIView, generics.DestroyAPIView):
# class SingleMenuItemView(viewsets.ModelViewSet):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

class BookingViewSet(generics.ListCreateAPIView):
# class BookingViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
