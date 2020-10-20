from django.contrib import admin
from django.urls import path
from . import views
from .views import DrugListView, stockingListView, modifyDrugUpdateView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', DrugListView.as_view(), name='home'),
    path('create/', views.createDrug, name='create'),
    path('addstock/<int:pk>/', views.addStock, name='addstock'),
    path('stocking/', stockingListView.as_view(), name='stocking'),
    path('modify/<int:pk>/', modifyDrugUpdateView.as_view(), name='modify'),
    path('stocked/', views.StockAdded, name='stocked'),
    path('sell/<int:pk>/', views.sellDrug, name='sell'),
    path('search/', views.search, name='search'),
    path('search/stock/', views.searchstock, name='searchstock'),
    path('history/', views.salehistory, name='history'),
    path('today/', views.todaysales, name='today'),
]
