from django.contrib import admin
from .models import Drug
from .models import Sale

admin.register(Drug,Sale)(admin.ModelAdmin)
# Register your models here.
