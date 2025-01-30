from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import Product, Payment, Category, CartItem, Cart, Brand
from django.contrib.auth.models import User



def signup(request):
    if request.method == 'POST':
        username = request.POST['signup_username']
        email = request.POST['signup_email']
        password1 = request.POST['signup_password1']
        password2 = request.POST['signup_password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=make_password(password1))
            user.set_password(password1)
            user.save()
            return redirect('login')
    return render(request, 'signup.html')



@login_required
def main(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return render(request, 'index.html', {'products': products, 'categories': categories, 'brands':brands})


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'details.html', {'product': product})

def logout_user(request):
    logout(request)
    return redirect('login')
  


def login_user(request):
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        user = authenticate(username=username, password=password)
        if user.is_authenticated:
            login(request, user)
            return redirect('landing')
        return render(request, 'login.html')
    return render(request, 'login.html')
                             