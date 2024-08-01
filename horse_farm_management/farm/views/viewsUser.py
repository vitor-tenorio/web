from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..forms.UserForms import UserForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def add_user(request):
    form = UserForm()
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            userName=form['userName'].value()
            firstName=form['firstName'].value()
            lastName=form['lastName'].value()
            email=form['email'].value()
            password=form['senha_1'].value()
            
            if User.objects.filter(username=userName).exists():
                return redirect('cadastro')
            else:
                user = User.objects.create_user(username=userName, first_name=firstName, last_name=lastName, email=email, password=password)
                user.save()
                return redirect('home')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')