from django.contrib import admin
from .models import Drug, Sale, Stocked


admin.register(Drug, Sale, Stocked)(admin.ModelAdmin)
# Register your models here.
