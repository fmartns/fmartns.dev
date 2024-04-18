from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import UserSocialMedia
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import ContactForm
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.translation import gettext as _

def index(request):
    return render(request, "index.html")

def user_links_page(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
        user_social_media = UserSocialMedia.objects.filter(user=user)
        user_profile = user.userprofile
        context = {
            'user': user,
            'user_social_media': user_social_media,
            'user_profile': user_profile
        }
    else:
        user = request.user
        user_profile = user.userprofile
        context = {
            'user': user,
            'user_profile': user_profile
        }

    return render(request, 'user.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            message = 'Mensagem de: {0} <{1}>\n\n{2}'.format(name, email, message)

            html_message = render_to_string('email/contact.html', {'name': name, 'email': email, 'message': message})

            send_mail(
                'Nova mensagem! (fmartns.dev) ', 
                message,
                'hello@fmartns.dev',
                ['hello@fmartns.dev'],
                html_message=html_message,
            )

            messages.success(request, _('Your message has been sent successfully!'))
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def terms(request):
    return render(request, 'terms.html')

def page_not_found(request, exception):
    return render(request, '404.html', status=404)