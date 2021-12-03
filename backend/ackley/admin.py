from django.contrib import admin

# Register your models here.
from .models import Album, Contacts,Bookings
admin.site.register(Contacts)
admin.site.register(Bookings)
admin.site.register(Album)
