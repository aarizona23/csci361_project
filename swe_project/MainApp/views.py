from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.hashers import make_password, check_password

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = UserProfile.objects.get(username=username)
        if check_password(password, user.password):
            if user.user_status == 1:
                return redirect('admin_page')
            else:
                return render(request, 'login.html', {'error': 'Invalid user_status'})
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    
def admin_page(request):
    return render(request, 'admin_page.html')
    

