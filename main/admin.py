from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Corredor, Propiedad

admin.site.register(Corredor)
admin.site.register(Propiedad)