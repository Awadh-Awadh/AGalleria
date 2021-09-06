from django.contrib import admin
from .models import Images, Cat,Location

# Registering models:
admin.site.register(Images)
admin.site.register(Cat)
admin.site.register(Location)
