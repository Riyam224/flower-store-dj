from django.shortcuts import render , get_object_or_404 , redirect
# add to fav and more 
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from django.utils import timezone
# send mail 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



def share(request):
    return render(request , 'store/share.html', {})

    
def home(request):
    products = Item.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']

        send_mail(
            name,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )

        messages.info(request , 'Thanks for contacting us !')

 
 
    context = {
        'products': products,
        
    }
    return render(request , 'store/home.html', context)


def flower_details(request , id):
    product = get_object_or_404(Item , id=id)
    is_favorite = False
    if product.favorite.filter(id=request.user.id).exists():
        is_favorite = True



    context = {
        'product': product,
        'is_favorite':  is_favorite,
       
    }


    return render(request , 'store/details.html', context)


def flower_fav(request , id):
    product = get_object_or_404(Item, id=id)

  
    if product.favorite.filter(id=request.user.id).exists():
        product.favorite.remove(request.user)
    else:
        product.favorite.add(request.user)
    
    context = {
        'product' : product
    }
    return HttpResponseRedirect('/')


def flower_fav_list(request):
    user = request.user
    favorite_flowers = user.favorite.all()
    context = {
        'favorite_flowers': favorite_flowers
    }
    
    return render(request , 'store/favorite_flowers.html', context)



def add_to_cart(request , slug):
    item = get_object_or_404(Item , slug=slug)
    order_item , created = OrderItem.objects.get_or_create(
        item=item ,
         user=request.user , 
         ordered=False)

    order_qs = Order.objects.filter(user=request.user , ordered=False)
    
    if order_qs.exists():
        order = order_qs[0]

        # check if the order item in the order 
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(orderitem)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user , 
        ordered_date=ordered_date)
        order.items.add(order_item)
       
    return redirect("store:flower_details",slug=slug)




def cart(request):
    return render(request , 'store/cart.html' , {})

def checkout(request):
    return render(request , 'store/checkout.html', {})