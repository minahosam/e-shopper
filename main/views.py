from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def show_all_product(request):
    all_brand=brand.objects.all()
    all_category=category.objects.all()
    all_products=index.objects.all().order_by('-id')[:6]
    return render(request,'main/index.html',{'all_brand':all_brand ,'all_category':all_category,'products':all_products})
def product_detail(request,slug):
    all_products=index.objects.get(slug=slug)
    all_brand=brand.objects.all()
    all_category=category.objects.all()
    all_reviews=review.objects.all()
    if request.method=='POST':
        form=reviewForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=reviewForm()
    return render(request,'main/product_details.html',{'products':all_products,'all_brand':all_brand ,'all_category':all_category,'form':form,'revi':all_reviews})
def wish_list(request,slug):
    product=index.objects.get(slug=slug)
    if request.user in product.add_to_wishlist.all():
        product.add_to_wishlist.remove(request.user)
    else:
        product.add_to_wishlist.add(request.user)
    return redirect('main:show')
def wishlist_page(request):
    product_wished=index.objects.filter(add_to_wishlist=request.user)
    return render(request,'main/wish_page.html',{'wished':product_wished})
def search_by_category(request):
    cat=request.GET['category']
    print (cat)
    all_brand=brand.objects.all()
    all_category=category.objects.all()
    name_of_category=category.objects.get(category_name=cat)
    categore_selected_result=index.objects.filter(product_category=name_of_category.id)
    return render(request,'main/search_category.html',{'category':categore_selected_result,'all_brand':all_brand ,'all_category':all_category})
def search_by_brand(request):
    brand_=request.GET['brand']
    print(brand_)
    all_brand=brand.objects.all()
    all_category=category.objects.all()
    brand_name=brand.objects.get(brand_name = brand_)
    brand_selected_result=index.objects.filter(product_brand=brand_name.id)
    return render(request,'main/search_brand.html',{'brand':brand_selected_result,'all_brand':all_brand ,'all_category':all_category})