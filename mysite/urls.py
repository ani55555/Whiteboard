"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from polls.views import *
from django.contrib.auth import views as auth_views


#know that path('password_reset/'...) is the builtin/generic django reset view -> CHANGE IT
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_try, name = 'homepage'),
    path('search/', search_try, name = 'trysearching'),
    path('profile/', profile_try, name = 'tryprofile'),
    path('signup/', signup_try.as_view(), name = 'signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('information/', information_try, name = 'tryinformation'),
    path('logout/', logout_try, name = 'tryloggingout'),
    path('login/', auth_views.login, name = 'login'),
    path('login_error/', login_error_handle, name = 'tryloginerror'),
    path('change_password/', auth_views.password_reset, name = 'passwordchangetry')
    #path('change_password/',
     #auth_views.PasswordChangeView.as_view(template_name = '')),

]
