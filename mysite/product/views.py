from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    categorys = category.objects.all().first()

    data ={
        'category':categorys
    }
    return render(request, 'home.html',data)


def about(request):
        return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def products(request):

    products = product.objects.all()

    datas ={
        'product':products
    }
    return render(request, 'products.html',datas)
