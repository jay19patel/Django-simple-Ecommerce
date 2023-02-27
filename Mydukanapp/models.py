from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    full_name=models.CharField(max_length=100)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    pin=models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    profile_imge=models.ImageField(upload_to ='images/userprofile/')
    def __str__(self):
        return self.full_name

class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(null=True)
    description =models.CharField(max_length=200)
    image=models.ImageField(upload_to ='images/products_images/')
    category =models.ManyToManyField(Tag)
    date_added=models.DateTimeField(auto_now_add=True,null=True)
    pices=models.FloatField(null=True)
    seller_name=models.CharField(max_length=100)
    offers=models.CharField(max_length=100)
    samples_image1=models.ImageField(upload_to ='images/samples_img/')
    samples_image2=models.ImageField(upload_to ='images/samples_img/')

    def __str__(self):
        return self.name


class OrderStatuse(models.Model):
    STATUS = (
        ('Panding','Panding'),
        ('Out of Delivery','Out of Delivery'),
        ('Delivered','Delivered'),

    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)
    date_orderd=models.DateTimeField(auto_now_add=True,null=True)
    transaction_id =models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True ,choices=STATUS,default="Panding")
    quntity=models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.status
    



class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total