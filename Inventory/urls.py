from django.contrib import admin
from django.urls import path
from . import views
from .views import DrugListView, stockingListView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', DrugListView.as_view(), name='home'),
    path('create/', views.createDrug, name='create'),
    path('addstock/<int:pk>/', views.addStock, name='addstock'),
    path('stocking/', stockingListView.as_view(), name='stocking'),
    path('sell/<int:pk>/', views.sellDrug, name='sell'),
    path('search/', views.search, name='search'),
    path('search/stock/', views.searchstock, name='searchstock'),
]
