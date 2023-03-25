from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import  json
import openai
from django.views import View
import datetime
from django.contrib import messages
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.generic.detail import DetailView





def nav(request):
    categories = Category.objects.all()
    return render(request, 'shop/landing.html', {'categories': categories})


def furniture_by_category(request, category_name):
    categories = Category.objects.all()
    category = Category.objects.get(name=category_name)
    furniture = Furniture.objects.filter(categories=category)
    p = Paginator(furniture, 5)
    page = request.GET.get('page', 1)
    objects_list = p.get_page(page)
    context = {
        'objects_list':objects_list,
        'category': category,
        'categories':categories,
        'furniture': furniture,
        'shipping':False,
    }
    return render(request, 'shop/category.html', context)

def user_logout(request):
    logout(request)
    return redirect('nav')


def register(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Register complete')
            return redirect('login')
        else:
            messages.error(request, 'Register not complete')
    else:
        form = UserRegisterForm()
        customer = Customer()
    return render(request, 'shop/register.html',{"form":form,'customer':customer,'categories':categories})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('nav')
    else:
            form = UserLoginForm()
    return render(request, 'shop/login.html',{"form":form,'title':'Restraunt'})


def cab(request):
    return  render(request,'shop/cabinet.html')



def cart(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user, defaults={'name': request.user.username, 'email': request.user.email})
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context = {'items':items,'order':order,'cartItems':cartItems,'shipping':False,'categories':categories}
    return render(request,'shop/cart.html',context)



def checkout(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items':items,'order':order,'cartItems':cartItems,'shipping':False,'categories':categories}
    return render(request,'shop/checkout.html',context)

class GeeksDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        furniture = get_object_or_404(Furniture, pk=kwargs['pk'])
        context = {'furniture': furniture}
        return render(request, 'shop/detail.html', context)


def upadateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('productId:', productId)
    print('action:', action)

    customer = request.user.customer
    product = Furniture.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()
    return  JsonResponse('Item was added',safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        print(data)

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                zipcode=data['shipping']['zipcode'],
            )

    else:
        print("User is not logged in!")
    return JsonResponse('Payment complete!', safe=False)

class ChatbotView(View):

    template_name = "shop/chat.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        prompt = request.POST.get('question')
        model = "text-davinci-002"
        openai.api_key='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' 

        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        context = {'response': response.choices[0].text}
        return render(request, self.template_name, context=context)



