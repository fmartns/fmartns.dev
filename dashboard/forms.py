from django import forms
from .models import SocialMedia, UserSocialMedia, UserProfile
from django.utils.translation import gettext_lazy as _

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = ['name', 'prefix', 'icon']

class UserSocialMediaForm(forms.ModelForm):
    class Meta:
        model = UserSocialMedia
        fields = ['social_media', 'username']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        if UserSocialMedia.objects.filter(user=self.user).count() >= 5:
            raise forms.ValidationError(_("You can only select up to 5 social media accounts."))
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()

        if self.cleaned_data.get('delete'):
            self.cleaned_data['delete'].delete()

        return instance

class UserProfileForm(forms.ModelForm):
    last_name = forms.CharField(required=False)
    primary_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    secondary_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    font_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'job', 'is_student', 'primary_color', 'secondary_color', 'font_color']

