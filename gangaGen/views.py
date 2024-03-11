from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import CustomUser

def home(request):
    return render(request, 'index.html')

def database(request):
    access_code = None

    if not request.user.is_authenticated:
        messages.error(request, "You are not logged in.")
        # return redirect('home')

    if request.method == "POST":
        access_code = request.POST.get("access_code")

    user = authenticate(request, access_code=access_code)

    if user is not None:
        login(request, user)
        masked_access_code =' '.join(list('⬤' * (len(access_code) - 2) + access_code[-2:]))
        return render(request, 'database.html', {'access_code': masked_access_code})
    else:
        messages.error(request, "Wrong Credentials")
        return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')
