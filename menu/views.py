# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http 	  import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from menu.forms import *
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from menu.models import *

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

# Create your views here.
def tidyTags(listT):
    ttt=[]
    for tagT in listT:
        T=tagT.replace("_", " ")
        T=T.capitalize()
        ttt.append(T)
    return ttt

def index(request):
	return render(request, 'index.html',{})

def menu(request):
	dishes = Dishes.objects.all()
	return render(request, 'menu.html',{"tab_title":"Menu list",
        "tab_description":"Discover a menu inspired by Mother Buongusto's simple, yet creative cuisine, as well as those wonderful old world traditional recipes.",'dishes':dishes})

#Login and sign in views
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/waiter/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request,'login.html',{})

def signin(request):
	if request.method =="POST":
		form = SigninForm(request.POST)
		if form.is_valid():
		   form.save()
		   return redirect('/login')
	else:
		form = SigninForm()

	return render(request,'signin.html',{'form': form})

#Customer views
def bookings(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookingForm(request.POST)
        form.as_table()
        form.save()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookingForm()
        form.as_table()

    dishes = Dishes.objects.all()

    return render(request, 'customer/bookings.html', {"tab_title":"Book now!",
		"tab_description":"Book your table now, come and enjoy our delicious Menu.", 'form': form, 'dishes':dishes})

def thanks(request):
	context={
		"tab_title":"Thanks for booking.",
		"tab_description":"See you soon!",
		}
	return render(request, 'customer/thanks.html',context)

def tables(request):
	tables_info = Tables.objects.all()
	return render(request,'tables.html',{'tables_info':tables_info})

#Waiter views
def waiter(request):
    # if this is a POST request we need to process the form data
	customers_info = []
	customers_query = Customers.objects.all().values()
	orders_info = []
	orders = Order.objects.exclude(category='payed').values()
	for customer_query in customers_query:
		features_c = list(customer_query.keys())
		customers_info.append(list(customer_query.values()))

	for order in orders:
		dish = Dishes.objects.get(id=order['dish_id'])
		table = Tables.objects.get(table=order['table_id'])

		dishName = dish.name
		dishPrice = dish.price
		quantity = order['quantity']
		orders_info.append([
            table.table,

            dishName,
            "$"+str(dishPrice),
            quantity,
            round(float(dishPrice)*quantity,2),
        ])

	context = {
	    'features_c':features_c,
		'customers_info':customers_info,
        'orders_info':orders_info,
        'features':['table','dish','price','quantity','subtotal'],
        'tab_title':'Waiter Dashboard',
        'tab_description':'Manage all customer orders'
    }
	return render(request, 'waiter/waiter.html', context)

class OrderView(FormView):
    template_name = 'waiter/waiter_add.html'
    form_class = OrderForm
    success_url = '/waiter/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
		#form.send_email()
        return super(OrderView, self).form_valid(form)

class CustomerView(FormView):
    template_name = 'waiter/waiter_add_customer.html'
    form_class = CustomerForm
    success_url = '/waiter/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
		#form.send_email()
        return super(CustomerView, self).form_valid(form)


class WaiterView(TemplateView):
    template_name = "waiter/waiter.html"


def create(request):
    order = Order(table=request.POST['table'], dish=request.POST['dish'], quantity=request.POST['quantity'])
    member.save()
    return redirect('waiter/')

def read(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'waiter/result.html', context)

def edit(request, id):
    order = Orders.objects.get(id=id)
    context = {'order': order}
    return render(request, 'waiter/edit.html', context)

def update(request, id):
    order = Orders.objects.get(id=id)
    order.table = request.POST['table']
    order.dish = request.POST['dish']
    order.quantity = request.POST['quantity']
    order.save()
    return redirect('waiter/')


def delete(request, id):
    order = Orders.objects.get(id=id)
    order.delete()
    return redirect('waiter/')

def cook(request):
	context={
		"tab_title":"Cook",
		"tab_description":"See all pending orders"
		}
	return render(request, 'cook/cook.html',context)

def boss(request):
	context={
		"tab_title":"Boss Dashboard",
		"tab_description":"Manage your business from everywhere"
		}
	return render(request, 'boss/boss.html',context)
