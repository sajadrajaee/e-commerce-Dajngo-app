from django.shortcuts import render
from .models import CustomUser
from .forms import CustomUserCreationForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            user = CustomUser.objects.create_user(
                username= username,
                email = email
            )
            user.set_password(password)
            user.save()
            return redirect("accounts:profile")
        raise ValueError("invalid form")
    form = CustomUserCreationForm(None)
    return render(request, 'accounts/signup.html', {"form":form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect('accounts:profile')
            raise ValueError("something went wrong!")
        raise ValueError("invalid form")
    form = LoginForm(None)
    return render(
        request, "accounts/login.html", {'form':form}
    )
            
def logout_view(request):
    logout(request)
    return redirect('products:index')

@login_required(login_url="accounts:login")
def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(
        request, 'accounts/profile.html', {"user":user}
    )