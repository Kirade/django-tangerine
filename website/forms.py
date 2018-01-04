from django import forms
from .models import Board, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title', 'text', )


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput,
    )

    address = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    full_name = forms.CharField(max_length=20)

    subscribe = forms.BooleanField(
        widget=forms.CheckboxInput,
    )

    class Meta:
        model = User
        fields = ('username','password1','password2', 'email', 'full_name', 'address', 'phone_number', 'subscribe')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)

        if commit:
            user.email = self.cleaned_data['email']
            user.save()

            profile = Profile.objects.get(user_id=user.id)
            profile.address = self.cleaned_data['address']
            profile.phone_number = self.cleaned_data['phone_number']
            profile.full_name = self.cleaned_data['full_name']
            profile.subscribe = self.cleaned_data['subscribe']
            profile.save()

        return user


class MyPageForm(RegisterForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'full_name', 'address', 'phone_number',)

