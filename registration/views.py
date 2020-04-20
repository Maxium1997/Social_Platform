from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.generic.base import TemplateView
from django.views.generic import CreateView

from Social_Platform.settings import LOGOUT_REDIRECT_URL

from registration.models import User
from registration.forms import UserSignupForm
from post.models import Collection

# Create your views here.


# def index(request):
#     user = request.user
#     context = {'user': user}
#     return render(request, 'index.html', context)
class Index(TemplateView):
    template_name = 'index.html'


# def sign_up(request):
#     pass
class SignUpView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'sign_up.html'

    def form_valid(self, form):
        user = form.save()
        Collection.objects.create(user=user)
        auth.login(self.request, user)
        return redirect('index')


# def login(request):
#     pass


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
