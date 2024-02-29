from django.contrib import admin
from .api.models import Booking, Menu, MenuItem, User

# Register your models here.
admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(User)