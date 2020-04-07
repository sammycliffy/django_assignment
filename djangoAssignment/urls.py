"""djangoAssignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from app import views
from app.forms import *
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^signup/$',views.SignUp_View.as_view(), name="signup"),
    url(r'^dsignup/$',views.Practitioner_View.as_view(), name="dsignup"),
    url(r'^statistics/$',views.statistics, name="statistics"),
    url(r'^records/$',views.records, name="records"),
    url(r'^filter/$',views.filters, name="filters"),
    url(r'^profile/$',views.profile_user, name="profile"),
    url(r'^medprofile/$',views.medprofile, name="medprofile"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="app/index.html"), name="logout"),
]
