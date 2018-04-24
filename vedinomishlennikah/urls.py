"""vedinomishlennikah URL Configuration

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

from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^user/', include('user.urls')),
    url(r'^admin/', admin.site.urls),
    path('main_app/', include('main_app.urls')), # чтобы перенаправить запросы с корневового URL, на URL приложения
    # path('event/', include('event.urls')), # чтобы перенаправить запросы с корневового URL, на URL приложения
    url(r'^$', RedirectView.as_view(url='/main_app/', permanent=True)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

