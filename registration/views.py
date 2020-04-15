from django.shortcuts import render, redirect
from django.contrib import auth

from Social_Platform.settings import LOGOUT_REDIRECT_URL

# Create your views here.


def index(request):
    user = request.user
    context = {'user': user}
    return render(request, 'index.html', context)


def sing_up(request):
    pass


def login(request):
    pass


def logout(request):
    auth.logout(request)
    return redirect(LOGOUT_REDIRECT_URL)


def profile(request):
    pass


def profile_update(request):
    pass


def email_verify(request):
    pass


def password_change(request):
    pass


def password_reset(request):
    pass
