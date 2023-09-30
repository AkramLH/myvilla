from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterCustomForm


# registering customer
def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer =True
            var.save
            messages.info(request, 'Akunmu telah berhasil di registrasi. Mohon Login')
            return redirect('login')
        else:
            messages.warning(request, 'Tolong cek kembali data anda')
            return redirect('register-customer')
    else:
        form = RegisterCustomForm()
        context = {
            'form':form
        }
        return render(request, 'users/register_cutomer.html', context)
    
# Login a user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'Selamat, Anda berhasil login')
            return redirect('dashboard')
        else:
            messages.warning(request,'periksa kembali data anda')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
# Logout a user
def logout_user(request):
    logout(request)
    messages.info(request, 'Anda telah logout')
    return redirect('login')