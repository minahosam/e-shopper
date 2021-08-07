from django.shortcuts import render,redirect
from .models import *
from .forms import *
from Profile.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
import datetime
from .utils import *
# Create your views here.
def show_all_product(request):
    all_brand=brand.objects.all()
    all_category=category.objects.all()
    all_products=index.objects.all().order_by('-id')[:6]
    if request.user.is_authenticated:
        cookieContent=cookieCart(request)
        item=cookieContent['items']
        net_total=cookieContent['net']
        total=cookieContent['total']
    else:
        cookieContent=cookieCart(request)
        item=cookieContent['items']
        net_total=0
        total=cookieContent['total']
    return render(request,'main/index.html',{'all_brand':all_brand ,'all_category':all_category,'products':all_products,'total':total})
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
def cart(request):
    if request.user.is_authenticated:
        cartData=dataCart(request)
        item=cartData['items']
        net_total=cartData['net']
        total=cartData['total']
    else:
        cookieContent=cookieCart(request)
        item=cookieContent['items']
        net_total=cookieContent['net']
        total=cookieContent['total']
    return render(request,'main/cart.html',{'items':item ,'net':net_total,'total':total})
def checkout(request):
    if request.user.is_authenticated:
        cartData=dataCart(request)
        item=cartData['items']
        net_total=cartData['net']
        total=cartData['total']
        coutries=cartData['countries']
        states=cartData['state']
        shipping_info=shippinginfo.objects.all()
        shiped=False
        for i in item:
            if i.item_order.order_completed ==False:
                shiped = True
    else:
        cookieContent=cookieCart(request)
        item=cookieContent['items']
        net_total=cookieContent['net']
        total=cookieContent['total']
        shipping_info=shippinginfo.objects.all()
        coutries=country.objects.all()
        shiped=False
        states=state.objects.filter(state_country__in=coutries)
    return render(request,'main/checkout.html',{'items':item , 'net':net_total,'total':total,'countries':coutries,'state':states,'shiped':shiped,'info':shipping_info})
def update_cart(request):
    additon=json.loads(request.body)
    product=additon['produactId']
    product_action=additon['action']
    print(product_action,product)
    selected_product=index.objects.get(id=product)
    order_owner=request.user
    requested_user=userprofile.objects.get(usrename=order_owner)
    Order , create=order.objects.get_or_create(order_customer=requested_user,order_completed=False)
    item , create=orderItem.objects.get_or_create(item_name=selected_product,item_order=Order)
    if product_action == 'add':
        item.item_quantity = item.item_quantity 
    elif product_action == 'add2':
        item.item_quantity = item.item_quantity + 1
    else:
        item.item_quantity  = item.item_quantity- 1
        print('-')
    item.save()
    print(item.item_quantity)
    if item.item_quantity == 0:
        item.delete()
    if product_action == 'delete':
        item.delete()
    return JsonResponse('added',safe=False)
def country_name_from_json(request,*args,**kwargs):
    selected_country=kwargs.get('country')
    states_according_to_country=list(state.objects.filter(state_country__country_name=selected_country).values())
    return JsonResponse({'data':states_according_to_country})
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def process_order(request):
    transaction_id2=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    print(data)
    print(transaction_id2)
    userc=request.user
    print(userc)
    if userc.is_authenticated:
        user=request.user
        print(user)
        customer=userprofile.objects.get(username=user)
        print(customer)
        Order=order.objects.get(order_customer=customer,order_compcleted=False)
        total=float(data['shippingData']['total'])
        print(total)
        order.transaction_id=transaction_id2
        item=orderItem.objects.filter(item_order=Order)
        net_total=sum([items.total_selected_item for items in item])
        if total == net_total:
            Order.order_completed=True
        Order.save()
        shiiping=shippinginfo.objects.create(
            shipping_user=customer,shipping_order=Order,shipping_mail=data['shippingData']['email'],
            title=data['shippingData']['title'],shipping_firstname=data['shippingData']['firstname'],shiping_middlename=data['shippingData']['middlename'],
            shipping_lastname=data['shippingData']['lastname'],shiping_adress1=data['shippingData']['adress1'],shipping_adress2=data['shippingData']['adress2'],
            shipping_zipcode=data['shippingData']['zipcode'],shipping_country=data['shippingData']['country'],shipping_state=data['shippingData']['state'],
            shipping_phone=data['shippingData']['phone'],shipping_mobile_number=data['shippingData']['mobile_number'],shipping_fax=data['shippingData']['fax']
        )
        shiiping.save()
    else:
        print('user not logged in')
    return JsonResponse('payment submitted.........',safe=False)