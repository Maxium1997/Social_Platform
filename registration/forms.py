from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from registration.models import User


class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
