from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login_page')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request,'Invalid password')
            return redirect('login_page')
        else:
            login(request, user)
            return redirect('home')
        
    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"Username already exists")
            return redirect('/register/')
        
        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username=username
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully!")

        return redirect('/register/')
    return render(request, 'register.html')


    
        
        

