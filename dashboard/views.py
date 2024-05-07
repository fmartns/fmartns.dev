from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserSocialMedia, SocialMedia, UserProfile
from .forms import UserSocialMediaForm, SocialMediaForm, UserProfileForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
import json  # Adicione esta linha
from django.db import models

@login_required
def dashboard (request):
    return render(request, "dashboard/index.html")

@login_required
def administration(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    return render(request, "dashboard/administration.html")

@login_required
def social_media_list(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    social_medias = SocialMedia.objects.all()
    return render(request, 'dashboard/social_media_list.html', {'social_medias': social_medias})

@login_required
def social_media_add(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = SocialMediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('social_media_list')
    else:
        form = SocialMediaForm()
    return render(request, 'dashboard/social_media_form.html', {'form': form})

@login_required
def social_media_delete(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    social_media = get_object_or_404(SocialMedia, pk=pk)
    if request.method == 'POST':
        social_media.delete()
        return redirect('social_media_list')
    return render(request, 'dashboard/social_media_confirm_delete.html', {'social_media': social_media})

@login_required
def manage_social_media(request):
    user_social_media = UserSocialMedia.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserSocialMediaForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('manage_social_media')
    else:
        form = UserSocialMediaForm(user=request.user)

    return render(request, 'dashboard/links.html', {'user_social_media': user_social_media, 'form': form})

# Adicione estas views para lidar com a ativação/inativação e exclusão
@login_required
def toggle_active(request):
    if request.method == 'POST':
        # Obtém o ID do item a ser ativado ou desativado da solicitação POST
        item_id = request.POST.get('id')

        try:
            # Tenta obter o objeto UserSocialMedia com o ID fornecido
            user_social_media = UserSocialMedia.objects.get(id=item_id)
            
            # Alterna o estado is_active do item
            user_social_media.is_active = not user_social_media.is_active
            user_social_media.save()

            return JsonResponse({'success': True})  # Retorne uma resposta JSON indicando sucesso
        except UserSocialMedia.DoesNotExist:
            return JsonResponse({'error': 'UserSocialMedia item does not exist'})  # Se o item não for encontrado, retorne um erro JSON
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})  # Se não for uma solicitação POST, retorne um erro JSON

@login_required
def delete_link(request):
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            id = request.POST.get('id')
            try:
                user_social_media = UserSocialMedia.objects.get(id=id)
                position = user_social_media.position
                user_social_media.delete()
                
                # Reordenar os itens restantes
                UserSocialMedia.objects.filter(position__gt=position).update(position=models.F('position') - 1)
                
                return JsonResponse({'message': 'Success'})
            except UserSocialMedia.DoesNotExist:
                return JsonResponse({'message': 'Item not found'}, status=404)
    return JsonResponse({'message': 'Failed'}, status=400)

@login_required
def reorder_links(request):
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            new_order = request.POST.getlist('draggable-element')
            # Atualizar a ordem no banco de dados
            for index, item_id in enumerate(new_order):
                try:
                    user_social_media = UserSocialMedia.objects.get(id=item_id)
                    user_social_media.position = index
                    user_social_media.save()
                except UserSocialMedia.DoesNotExist:
                    return JsonResponse({'message': 'Item not found'}, status=404)
            return JsonResponse({'message': 'Success'})
    return JsonResponse({'message': 'Failed'}, status=400)

@login_required
def user_links(request):
    user_social_media = UserSocialMedia.objects.filter(user=request.user)
    return render(request, 'user_links.html', {'user_social_media': user_social_media})

@login_required
def user_social_media_delete(request, pk):
    user_social_media = get_object_or_404(UserSocialMedia, pk=pk)
    if request.method == 'POST':
        user_social_media.delete()
        return redirect('manage_social_media')
    return render(request, 'dashboard/user_social_media_confirm_delete.html', {'user_social_media': user_social_media})

@login_required
def manage_preferences(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, _('Settings saved successfully!'))
            return redirect('manage_preferences')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'dashboard/profile.html', {'form': form})

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('change_password')

    def form_valid(self, form):
        messages.success(self.request, _('Your password has been changed successfully!'))
        return super().form_valid(form)