from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Home view
def home_interface(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('log_in')

# Register view
def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password or not confirm_password:
            messages.warning(request, "All fields are required.")
            return redirect('register')

        if password != confirm_password:
            messages.warning(request, "Passwords do not match.")
            return redirect(register)

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username is already taken.")
            return redirect(register)

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email is already registered.")
            return redirect(register)

        if ' ' in username:
            messages.warning(request, "Username cannot contain spaces.")
            return redirect(register)
        
        if len(password) < 8:
            messages.warning(request, "Password must be at least 8 characters")
            return redirect(register)

        if not (email.endswith('@gmail.com') and email[0].isalpha()):
            messages.warning(request, "Enter a valid email")
            return redirect(register)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Your account has been created successfully. You can now log in.")
        return redirect('log_in')

    return render(request, 'register.html')

# Login view
def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect('admin_home')
            else:
                login(request,user)
                return redirect('home')
        
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('log_in')

    return render(request, 'login.html')

# Logout view
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have successfully logged out.")
    return redirect('log_in')
