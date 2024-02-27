from django.contrib import admin
from .api.models import Booking, Menu, User

# Register your models here.
admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(User)