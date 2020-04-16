from django.urls import path, include
from django.contrib.auth.views import LoginView


from registration import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout, name='logout'),

    path('accounts/', include([
        path('signup/', views.SignUp.as_view(), name='sign_up'),
        path('edit/', views.profile_update, name='profile_update'),
        path('password/change/', views.password_change, name='password_change'),
        path('password/reset/', views.password_reset, name='password_reset'),
    ])),

    path('email/verify/', views.email_verify, name='email_verify'),
]