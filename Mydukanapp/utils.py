import json
from .models import *

def SessionCart(request):
    product = request.POST.get('itemid')
    cart= request.session.get('cart')
        # request.session.get('cart').clear
    if cart:
        quantity = cart.get(product)
        if quantity:
            cart[product] = quantity+1
        else:
            cart[product] = 1
    else:
        cart = {}
        cart[product] = 1
        
    items =[]
    order ={'get_cart_total':0,'get_cart_items':0}
    cartitem=order['get_cart_items']

    request.session['cart']=cart
    

    for i in cart:
        
        cartItems += cart[i]['quantity']
        product = Products.objects.get(id=i)
        total = (product.price * cart[i]['quantity'])
        order['get_cart_total'] += total
        order['get_cart_items'] += cart[i]['quantity']
        item = {
				'id':product.id,
				'product':{
					'id':product.id,'name':product.name,'price':product.price}, 
				'quantity':cart[i]['quantity'],
				'get_total':total,
				}
        items.append(item)
    return {'cartItems':cartItems ,'order':order, 'items':items}

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		cookieData = SessionCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	return {'cartItems':cartItems ,'order':order, 'items':items,'customer':customer}


