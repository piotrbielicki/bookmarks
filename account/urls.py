from django.conf.urls import url
from . import views

urlpatterns = [
    #Poprzedni widok logowania.
    #url(r'^login/$', views.user_login, name='login'),

    #Wzorce adresów RL dla widoków logowania i wylogowywania.
    url(r'^login/$',
                'django.contrib.auth.views.login',
                name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),
    url(r'^logout-then-login/$',
        'django.contrib.auth.views.logout_then_login',
        name='login_then_logout'),
    url(r'^$', views.dashboard, name='dashboard'),
]
