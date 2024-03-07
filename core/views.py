from django.shortcuts import render

# Create your views here.

# 1. Home page
def home(request):
    config = {
        'home': 'hello'
    }
    return render(request, 'index.html', config)

# 2. Register page
def register(request):
    config = {
        'data': 'register Data'
    }
    return render(request, 'register.html', config)

# 3. Login page
def login(request):
    config = {
        'data': 'Login Data'
    }
    return render(request, 'login.html', config)
