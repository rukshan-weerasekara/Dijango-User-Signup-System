from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm
from .models import User

def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # Redirect based on the role
            if user.role == 'normal_user':
                return redirect('normal_user_home')
            elif user.role == 'hotel_admin':
                return redirect('hotel_admin_dashboard')
            elif user.role == 'main_admin':
                return redirect('main_admin_dashboard')
            else:
                return redirect('signin')  # Fallback in case role is not found
    else:
        form = UserSignupForm()

    return render(request, 'users/signup.html', {'form': form})

# Sign In View
def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'normal_user':
                return redirect('normal_user_home')
            elif user.role == 'hotel_admin':
                return redirect('hotel_admin_dashboard')
            elif user.role == 'main_admin':
                return redirect('main_admin_dashboard')
        else:
            return render(request, 'users/signin.html', {'error': 'Invalid credentials'})
    return render(request, 'users/signin.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('signin')

# Dashboards
@login_required
def normal_user_home(request):
    return render(request, 'users/normal_user_home.html')

@login_required
def hotel_admin_dashboard(request):
    return render(request, 'users/hotel_admin_dashboard.html')

@login_required
def main_admin_dashboard(request):
    return render(request, 'users/main_admin_dashboard.html')





