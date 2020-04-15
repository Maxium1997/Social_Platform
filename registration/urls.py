from django.urls import path, include


from registration import views


urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('accounts/', include([
        path('signup/', views.sing_up, name='sign_up'),
        path('edit/', views.profile_update, name='profile_update'),
        path('password/change/', views.password_change, name='password_change'),
        path('password/reset/', views.password_reset, name='password_reset'),
    ])),
    path('email/verify/', views.email_verify, name='email_verify'),
]