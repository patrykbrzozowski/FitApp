from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe

from .forms import CustomUserCreationForm

def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Pomyślnie zarejestrowano użytkownika o adresie email: {form.cleaned_data["email"]}')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, mark_safe(f'Jesteś już zalagowany/a jako <b>{request.user.username}</b>'))
        return redirect('website:dashboard')

    username = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            #messages.success(request, f'User {user.username} logged is succesfully')
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('website:dashboard')
        else:
            messages.warning(request, 'Could not authentivte, zle dane')
    
    context = {}

    return render(request, 'accounts/login.html', context={'username': username})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

