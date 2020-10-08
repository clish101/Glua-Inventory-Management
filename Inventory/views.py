from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Drug
from .models import Sale
from .forms import DrugCreation
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime, timedelta, time

# Create your views here.


class DrugListView(ListView):
    model = Drug
    template_name = "Inventory/home.html"
    context_object_name = 'drugs'
    paginate_by = 5
    ordering = ['name']
    

@login_required
def createDrug(request):
    try:
        if request.method == 'POST':
            form = DrugCreation(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                form.save()
                messages.success(
                    request, f'{name} has been successfully added to the inventory')
                return redirect('create')
        else:
            form = DrugCreation()

        context = {'form': form}
        return render(request, 'Inventory/create.html', context)
        
    except:
        messages.success(request, 'Seems like the drug is already part of the inventory')
        return redirect('create')

@login_required
def addStock(request, pk):
    drug = Drug.objects.get(id=pk)
    amount_added = int(request.POST.get('added'))
    drug.stock += amount_added
    drug.save()
    messages.success(request, f'{amount_added} {drug.name} added')
    return redirect('stocking')


class stockingListView(ListView):
    model = Drug
    context_object_name = 'drugs'
    paginate_by = 5
    template_name = 'Inventory/stock.html'
    ordering = ['name']


@login_required
def sellDrug(request, pk):
    price=request.GET.get('sellAt')
    drug = Drug.objects.get(id=pk)
    drug.selling_price = price
    drug.stock -= 1
    drug.save()
    print(price)
    Sale.objects.create(seller=request.user,drug_sold=drug, sale_price=drug.selling_price, buying_price=drug.buying_price).save()
    messages.success(request, f'One {drug.name} sold')
    return redirect('home')

def search(request):
    drugs = Drug.objects.all().order_by('name')
    query = request.POST.get('q')

    if query:
        drugs = Drug.objects.filter(Q(name__icontains=query))

    context = {'drugs':drugs}
    return render(request, 'Inventory/home.html', context)

def searchstock(request):
    drugs = Drug.objects.all().order_by('name')
    query = request.POST.get('s')

    if query:
        drugs = Drug.objects.filter(Q(name__icontains=query))

    context = {'drugs':drugs}
    return render(request, 'Inventory/stock.html', context)

def salehistory(request):
    start_date=request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
    
        sales = Sale.objects.filter(date_sold__range=[start_date, end_date]).order_by('-date_sold')
        if sales:
            total_purchases = sales.aggregate(Sum('buying_price'))
            total_sales = sales.aggregate(Sum('sale_price'))

            bought_at = total_purchases.get('buying_price__sum')
            sold_at = total_sales.get('sale_price__sum')

            profit = sold_at - bought_at
        else:
            messages.success(request, 'Sorry no sales were done within those dates')
            return redirect('history')
        
        
    else:
        today = datetime.now().date()
        yesterday3 = today + timedelta(-2)
        start_date = datetime.combine(yesterday3, time())
        end_date = datetime.combine(today, time())

        sales = Sale.objects.filter(date_sold__range=[start_date, end_date]).order_by('-date_sold')
        total_purchases = sales.aggregate(Sum('buying_price'))
        total_sales = sales.aggregate(Sum('sale_price'))

        bought_at = total_purchases.get('buying_price__sum')
        sold_at = total_sales.get('sale_price__sum')

        profit = sold_at - bought_at
        

    context = {'sales': sales, 'profit':profit}
    context.update(total_sales)
    return render(request, 'Inventory/history.html', context)

def todaysales(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    start_date = datetime.combine(today, time())
    end_date = datetime.combine(tomorrow, time())

    if start_date and end_date:
    
        sales = Sale.objects.filter(date_sold__range=[start_date, end_date]).order_by('-date_sold')
        if sales:
            total_purchases = sales.aggregate(Sum('buying_price'))
            total_sales = sales.aggregate(Sum('sale_price'))

            bought_at = total_purchases.get('buying_price__sum')
            sold_at = total_sales.get('sale_price__sum')

            profit = sold_at - bought_at
        else:
            return messages.success(request, 'Sorry no sales were done within those dates')
    else:
        sales = Sale.objects.all().order_by('-date_sold')
        total_purchases = sales.aggregate(Sum('buying_price'))
        total_sales = sales.aggregate(Sum('sale_price'))

        bought_at = total_purchases.get('buying_price__sum')
        sold_at = total_sales.get('sale_price__sum')

        profit = sold_at - bought_at

    context = {'sales': sales,'profit':profit}
    context.update(total_sales)
    return render(request, 'Inventory/today.html', context)
