from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, SearchBar
from django.contrib.auth.models import User
from .models import Customer, Product, Tag, Order, ProductOrder
from .filters import ProductFilter, ProductSearch
from django.db.models import Q
from django.utils.crypto import get_random_string
import string

# Function
def searchfunction(request, form) :
    if request.GET :
        form = SearchBar(request.GET)
        if form.is_valid() :
            search = form.cleaned_data['search']
            return search.replace('/',' ')
    return None

def searchbar(search) :
    search_lst = search.split(" ")
    product_set = []
    
    for i in search_lst :
        products = Product.objects.filter(
            Q(name__icontains=i) |
            Q(tags__name__icontains=i)
        ).distinct()

        for product in products :
            product_set.append(product)
    
    return list(set(product_set))



# Create your views here.

def productPageAll(request) :
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    form = SearchBar()
    search_res = searchfunction(request, form)
    if search_res :
        return redirect(productPage, search_res)

    context = {
        'form' : form,
        'products' : f.qs & Product.objects.all(),
        'filters' : f
    }
    return render(request, 'website/productPage.html', context)

def productPage(request, search) :
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    form = SearchBar()
    search_res = searchfunction(request, form)
    if search_res :
        return redirect(productPage, search_res)

    filter_qs = [i for i in f.qs]
    products = searchbar(search)
    context = {
        'form' : form,
        'products' : set(products) & set(filter_qs),
        'filters' : f
    }
    return render(request, 'website/productPage.html', context)

def landingPage(request) :
    #Searchbar form
    form = SearchBar()
    search_res = searchfunction(request, form)
    if search_res :
        return redirect(productPage, search_res)

    popularTag = Tag.objects.filter(popular=True)
    product = Product.objects.all()

    context = {
        'form' : form,
        'popularTag' : popularTag,
        'products' : product
    }
    return render(request, 'website/landingPage.html', context)

def registerPage(request) :
    if request.user.is_authenticated :
        return redirect ('landingPage')

    form = RegisterForm()
    if request.method == "POST" :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            login(request, authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1']))
            return redirect('emailVerification')

    context = {'form' : form}
    return render(request, 'website/register.html', context)

def emailVerification(request) :
    if request.user.is_authenticated :
        user = Customer.objects.get(username=request.user.get_username())
        if user.email_verification :
            return render(request, 'website/emailConfirmation.html')
        else : 
            subject = 'Email Verification'
            message = 'Please go to this link \nlocalhost:8000/email-verification/' + user.email_verification_key
            from_mail = settings.EMAIL_HOST_USER
            to_list = [request.user.email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_mail, to_list, fail_silently=False)
            return render(request, 'website/emailVerification.html')
    return redirect('login')

def confirmedEmail(request, name) :
    user = Customer.objects.get(username=request.user.get_username())
    if user.email_verification_key == name :
        user.email_verification = True
        user.save()
    return redirect("emailVerification")

def detailproduct(request, id) :
    #Search Bar
    form = SearchBar()
    search_res = searchfunction(request, form)
    if search_res :
        return redirect(productPage, search_res)


    #Rate Function
    rate = 0
    product = Product.objects.get(id=id) 
    for i in product.review.all() :
        rate += i.rate

    if rate == 0 :
        product.rate = rate

    else :
        rate = round(rate/len(product.review.all()) * 2) /2
        product.rate = rate
        
    
    context = {
        'product' : product,
        'form' : form,
        'added_cart' : False,
        'added_wishlist' : False,
    }

    #Cart function
    if request.GET.get('cart') :
        if request.user.is_authenticated :
            return redirect('cartPage')
        else :
            return redirect('login')
    
    #Wishlist function
    if request.GET.get('wishlist') :
        if request.user.is_authenticated :
            return redirect('wishlistPage')
        else :
            return redirect('login')

    #Add to cart Function
    if request.GET.get('add_to_cart') :
        if request.user.is_authenticated :
            qty = request.GET.get('qty')
            cust = Customer.objects.get(username=request.user.username)


            cart_id = ''

            for i in cust.cart.all() :
                if i.product.id == int(id) :
                    cart_id = i

            if cart_id != "" :
                cart_id.qty += int(qty)
                cart_id.save()
                context['added_cart'] = True
            else : 
                productOrder = ProductOrder(product=Product.objects.get(id=id), qty=qty, price=Product.objects.get(id=id).price*float(qty))
                productOrder.save()
                cust.cart.add(productOrder)
                context['added_cart'] = True
        else :
            return redirect('login')

    #Add to wishlist function 
    if request.GET.get('add_to_wishlist') :
        if request.user.is_authenticated :
            cust = Customer.objects.get(username=request.user.username)
            cust.wishlist.add(Product.objects.get(id=id))
            context['added_wishlist'] = True
        else :
            return redirect('login')

    #Buy Now Function
    if request.GET.get('buy_now') :
        if request.user.is_authenticated :
            qty = request.GET.get('qty')
            cust = Customer.objects.get(username=request.user.username)
            product = Product.objects.get(id=id)
            order = None
            productOrder = ProductOrder.objects.filter(product=product, qty=qty, price=product.price*float(qty))
            if productOrder :
                productOrder = productOrder[0]
                order = Order(order_id=get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits), customer=cust, totalPrice=productOrder.price)
                order.save()
                order.product.add(productOrder)
                return redirect('checkout', order.order_id)
            else :
                productOrder = ProductOrder(product=product, qty=qty, price=product.price*float(qty))
                productOrder.save()
                order = Order(order_id=get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits),customer=cust, totalPrice=productOrder.price)
                order.save()
                order.product.add(productOrder)
                return redirect('checkout', order.order_id)
        else :
            return redirect('login')
    return render(request, 'website/detailproduct.html', context)

def cartPage(request) :
    #Search Bar
    form = SearchBar()
    search_res = searchfunction(request, form)
    if search_res :
        return redirect(productPage, search_res)
    
    cust= Customer.objects.get(username=request.user.username)
    price = 0
    for i in cust.cart.all() :
        price += i.price

    #Delete Button
    if request.POST.get('delete') :
        productOrder_id_list = request.POST.getlist('checkbox')
        for productOrder_id in productOrder_id_list :
            cust.cart.remove(ProductOrder.objects.get(id=productOrder_id))
    
    #Buy Now Button
    if request.POST.get('buynow') :
        order = Order(order_id=get_random_string(12, allowed_chars=string.ascii_uppercase + string.digits), customer=cust, totalPrice=price)
        order.save()
        for productOrder in cust.cart.all() :
            order.product.add(productOrder)
        return redirect('checkout', order.order_id)

    #Cancel or Delete All
    if not cust.cart.all().exists() or request.POST.get('cancel'):
        cust.cart.all().delete()
        return redirect('landingPage')

    context = {
        'form' : form,
        'cust' : cust,
        'price' : price
    }
    return render(request, 'website/cartPage.html', context)

def checkout(requset, id) :
    order = Order.objects.get(order_id=id)
    order.status = 'waiting_for_payment'
    order.save()
    return HttpResponse('ini checkout page')

def wishlistPage(request) :
    return HttpResponse('ini wishlist page')


