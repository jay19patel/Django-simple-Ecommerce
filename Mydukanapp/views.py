from django.http import JsonResponse
from .models import *
from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .utils import SessionCart, cartData
# ------------------------------------ login system ------------------------------------------

def Loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        userdata=auth.authenticate(request,username=username,password=password1)
        if userdata is not None:
            auth.login(request,userdata)
            return redirect('Homepage')
        else:
            messages.error(request,"sorry data not found")

    context={}
    return render(request,"loginsystem/loginpage.html",context)

def Logout(request):
    auth.logout(request)
    return redirect('Loginpage')

def Registrationpage(request):
    if request.method=='POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        city = request.POST.get('city')

        if (password1!= password2):
            messages.error(request, " Passwords do not match")
            return redirect('Registrationpage')
        else:
            myuser = User.objects.create_user(username, email, password1)
            myuser.save()
            messages.success(request, " Your iCoder has been successfully created")
            return redirect('Loginpage')
    context={}
    return render(request,"loginsystem/regist.html",context)

# ------------------------------------------------------------
def Homepage(request):
    catagory = Tag.objects.all()
    id = request.GET.get('id')
    if id:
        products=Products.objects.filter(category=id)
    else:
        products = Products.objects.all()


    context={'products':products,'catagory':catagory}
    return render(request,"shop/Homepage.html",context)


def Category(request):
    context={}
    return render(request,"shop/Homepage.html",context)

def Productdetails(request,id):
    Product=Products.objects.get(id=id)        
    context={'product':Product}
    return render(request,"shop/Productdetails.html",context)

def Cartpage(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,"shop/Cartpage.html",context)

@login_required(login_url=Loginpage)
def Checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,"shop/Checkoutpage.html",context)

@login_required(login_url=Loginpage)
def Payment(request):
    context={}
    return render(request,"shop/Payment.html",context)

def Statuspage(request):    
    data = cartData(request)
    customer=data['customer']
    items = data['items']
    status = OrderStatuse.objects.filter(customer=customer.id)

    context={'status':status,'items':items}
    return render(request,"shop/Statuspage.html",context)


