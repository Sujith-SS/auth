from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q  
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def admin_interface(request):
    if request.user.is_superuser:
        user=User.objects.all().order_by('date_joined')
        return render (request,'admin.html',{'users':user})
    return redirect('home')



# Create user
@csrf_protect
def createuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check for missing fields
        if not username or not email or not password or not confirm_password:
            messages.warning(request, "All fields are required.")
            return redirect(admin_interface)

        # Check for existing username
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username is already taken.")
            return redirect(admin_interface)

        # Check for existing email
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email is already registered.")
            return redirect(admin_interface)

        # Check if passwords match
        if password != confirm_password:
            messages.warning(request, "Passwords do not match.")
            return redirect(admin_interface)

        # Check for spaces in username
        if ' ' in username:
            messages.warning(request, "Username cannot contain spaces.")
            return redirect(admin_interface)

        # Check password length
        if len(password) < 8:
            messages.warning(request, "Password must be at least 8 characters.")
            return redirect(admin_interface)

        # Check for valid Gmail address
        if not email.endswith('@gmail.com') or not email[0].isalpha():
            messages.warning(request, "Enter a valid Gmail address.")
            return redirect(admin_interface)

        # Create and save the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "User created successfully.")
        return redirect(admin_interface)

    return redirect(admin_interface)

# Delete user
def delete_user(request,id):
    if request.method == "POST" and User.objects.filter(is_superuser=False):
        del_user = User.objects.get(id=id)
        del_user.delete()
        User.objects.filter(is_superuser=True)
        User.objects.all().order_by('username')
    return redirect(admin_interface)

# Admin search
def admin_search(request):
    if request.method == 'POST':
        user_details = request.POST.get('search')
        if user_details:
            users = User.objects.filter(username__icontains=user_details).order_by('username')
        else:
            users = User.objects.all().order_by('username')
        return render(request, 'admin.html', {'users': users})
    else:
        users = User.objects.all().order_by('username')
        return render(request, 'admin.html', {'users': users})
        
# Edit user
def edit_user(request,id):
    user = get_object_or_404(User,id = id)
    if request.method == "POST":
        # user = User.objects.get(id = id)
        name = request.POST.get('username')
        email = request.POST.get('user_email')
        # password = request.POST['password']
        # confirm_pass = request.POST['confirm_password']

        try:
            if User.objects.filter(~Q(id = id),email = email).get():
                messages.warning(request,"email is taken")
                return redirect (admin_interface)
        except:
            pass
        try:
            if User.object.get(username = name):
                messages.warning(request,"username is taken")
                return redirect(admin_interface)
        except:
            pass
           
        user.username = name
        user.email = email
        user.save()
        return redirect(admin_interface)