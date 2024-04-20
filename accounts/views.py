from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .decorators import anonymous_required
from dashboard.models import UserProfile
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm
import re

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
class CustomUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        if not re.match('^[a-z0-9]+$', username):
            raise forms.ValidationError(_('The username can only contain letters and numbers.'))
        if len(username) > 30:  # limite de 30 caracteres
            raise forms.ValidationError(_('The username cannot have more than 30 characters.'))
        return username

@anonymous_required
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
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
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})