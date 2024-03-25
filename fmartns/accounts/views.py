from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .decorators import anonymous_required
from dashboard.models import UserProfile

@anonymous_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'registration/login.html') 
    return render(request, 'registration/login.html')

@anonymous_required
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = request.POST.get('email', '')
            user.save()

            UserProfile.objects.create(
                user=user,
                first_name=user.username,
                job="Developer",
                is_student=False,
                primary_color="#10F0DE",
                secondary_color="#2B323C",
                font_color="#FFFFFF"
            )

            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})