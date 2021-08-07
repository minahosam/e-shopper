from .models import *
import json
def cookieCart(request):
    try:
        Cart=json.loads(request.COOKIES['cart'])
    except :
        Cart={}
    print(Cart)
    item=[]
    net_total=0
    total=0
    for i in Cart:
        try:
            item_quantity=Cart[i]['quantity']
            print(item_quantity)
            select_product=index.objects.get(id=i)
            print(select_product)
            all=(select_product.product_price * item_quantity)
            print(all)
            net_total+=all
            print(net_total)
            total += item_quantity
            item1={
                'item_name':{
                    'id':select_product.id,
                    'product_name':select_product.product_name,
                    'product_photo':select_product.product_photo,
                },
                'item_quantity':item_quantity,
                'total_selected_item':all,
            }
            item.append(item1)
            if index.product_digital == False:
                order.order_completed = True
        except :
            pass
    return {'items':item ,'net':net_total,'total':total}
def dataCart(request):
    order_owner=request.user
    requested_user=userprofile.objects.get(usrename=order_owner)
    order_owner_id=request.user.id
    print(order_owner_id)
    Order , create=order.objects.get_or_create(order_customer=requested_user,order_completed=False)
    # item=Order.orderitem_set.all()
    item=orderItem.objects.filter(item_order=Order)
    net_total=sum([items.total_selected_item for items in item])
    total=sum([items.item_quantity for items in item])
    coutries=country.objects.all()
    states=state.objects.filter(state_country__in=coutries)

    return {'items':item ,'net':net_total,'total':total,'countries':coutries,'state':states}