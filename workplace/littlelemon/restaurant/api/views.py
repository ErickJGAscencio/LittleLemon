from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework import response
from rest_framework import status

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#   permission_classes = [IsAuthenticated]
#   def list(self, request):
#     queryset = User.objects.all()
#     # serializer = UserSerializer(queryset, many=True)
#     serializer = UserSerializer(queryset, many=True)
#     return response(serializer.data)

#   def retrieve(self, request, pk=None):
#     # Implementación para recuperar un usuario específico por su clave primaria (pk)
#     queryset = User.objects.get(pk=pk)  # Suponiendo que User es tu modelo de usuario
#     serializer = UserSerializer(queryset)
#     return response(serializer.data)

#   def create(self, request):
#     # Implementación para crear un nuevo usuario
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return response(serializer.data, status=status.HTTP_201_CREATED)
    
#     return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   def update(self, request, pk=None):
#     # Implementación para actualizar un usuario existente por su clave primaria (pk)
#     user = User.objects.get(pk=pk)  # Suponiendo que User es tu modelo de usuario
#     serializer = UserSerializer(user, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return response(serializer.data)
    
#     return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   def destroy(self, request, pk=None):
#     # Implementación para eliminar un usuario existente por su clave primaria (pk)
#     user = User.objects.get(pk=pk)  # Suponiendo que User es tu modelo de usuario
#     user.delete()
#     return response(status=status.HTTP_204_NO_CONTENT)
