from django.contrib import admin
from .models import Drug, Sale, Stocked, Category, Measurement


admin.register(Drug, Sale, Stocked, Category, Measurement)(admin.ModelAdmin)
# Register your models here.
