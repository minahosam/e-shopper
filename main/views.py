from django.shortcuts import render
from .models import *
# Create your views here.
def show_all_product(request):
    all_brand=brand.objects.all()
    all_category=category.objects.all()
    all_products=index.objects.all().order_by('-id')[:6]
    return render(request,'main/index.html',{'all_brand':all_brand ,'all_category':all_category,'products':all_products})
def product_detail(request,slug):
    all_products=index.objects.get(slug=slug)
    return render(request,'main/product_details.html',{'products':all_products})