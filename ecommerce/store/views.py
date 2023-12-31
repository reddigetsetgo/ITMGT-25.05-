from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from . models import Product
from .forms import OrderForm, CreateUserForm
#rom .filters import OrderFilter
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages


all_products = [
	{
		"slug": "Reverence Hand Wash",
    	"title": "Reverence Aromatique Hand Wash",
    	"image": "Capture-2023-07-20-184008.png ",
    	"price": 41.00,
    	"description": "An unorthodox aromatic blend with botanical extracts and finely milled Pumice, to gently cleanse, exfoliate, and leave the hands smooth, purified, and refreshed.",
  	},
  	{
    	"slug": "Reverence Hand Balm",
    	"title": "Reverence Aromatique Hand Balm",
    	"image": "Capture-2023-07-20-184307.png",
    	"price": 33.00,
    	"description": "A rich, skin-softening balm containing carefully selected emollient ingredients, including Potassium Lactate, to soften the skin and provide sustained hydration.",
  	},
  	{
   		"slug": "Geranium Body Scrub",
    	"title": "Geranium Leaf Body Scrub",
    	"image": "Capture-2023-07-20-184438.png",
    	"price": 37.00,
    	"description": "An invigorating body exfoliant that leaves the skin thoroughly cleansed and immaculately smooth—perfectly prepared for hydration.",
  	},
  	{
    	"slug": "Geranium Body Cleanser",
    	"title": "Geranium Leaf Body Cleanser",
    	"image": "Capture-2023-07-20-184559.png",
    	"price": 47.00,
    	"description": "An invigorating cleansing gel that gently banishes grime and provides an agreeable alternative to conventional soap.",
	},
	{
		"slug": "Serum",
    	"title": "Lightweight Facial Hydrating Serum",
    	"image": "Capture-2023-07-20-185135.png",
    	"price": 125.00,
    	"description": "A light, rapidly absorbed formulation with a soothing base of Aloe Vera; ideal for those who avoid heavier hydrators.",
	},
	{
		"slug": "Exfoliant",
    	"title": "Purifying Facial Exfoliant Paste",
    	"image": "Capture-2023-07-20-184841.png",
    	"price": 57.00,
    	"description": "A cream-based cleansing formulation enhanced with fine Quartz and Lactic Acid to slough away dead skin cells and soften the skin.",
	},

]

def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Account Created')
			return redirect('login')

	context = {'form':form}
	return render(request, 'store/register.html', context)

def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('store')
		else: 
			messages.info(request, 'Username or Password is Incorrect')

	context = {}
	return render(request, 'store/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def product_Detail(request,slug):
	data = cartData(request)
	cartItems = data['cartItems']
	context = {'cartItems':cartItems}

	identified_product = next(product for product in all_products if product['slug'] == slug)
	#eturn render(request, "store/product_detail.html", context)

	return render(request, "store/product_detail.html", context, {
    "product": identified_product
  })

def store(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

def index(request):
	if 'q' in request.GET:
		q = request.GET['q']
		data = Product.objects.filter(name__icontains=q)
	else:
		data = Product.objects.all()
	context = {
		'data': data
	}
	return render(request,'store/store.html', context)

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)