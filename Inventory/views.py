from django.shortcuts import render, redirect
from .models import Drug
from .forms import DrugCreation
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


class DrugListView(ListView):
    model = Drug
    template_name = "Inventory/home.html"
    context_object_name = 'drugs'
    paginate_by = 5
    ordering = ['name']
    
    # def get_queryset(self):
        
    #     return search()


# def home(request):
#     drugs = Drug.objects.all()
#     context = {'drugs': drugs}
#     return render(request, 'Inventory/home.html', context)

@login_required
def createDrug(request):
    if request.method == 'POST':
        form = DrugCreation(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            form.save()
            messages.success(
                request, f'{name} has been successfully added into the inventory')
            return redirect('create')
    else:
        form = DrugCreation()

    context = {'form': form}
    return render(request, 'Inventory/create.html', context)

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
    drug = Drug.objects.get(id=pk)
    drug.stock -= 1
    drug.save()
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