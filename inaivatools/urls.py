"""inaivatools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic.base import TemplateView
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    #path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('expandeduser.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('merge/', include('mergetextlines.urls')),
    path('format/', include('formattelnumbers.urls')),
    path('compare/', include('comparelists.urls')),
    path('split/', include('splittextbychar.urls')),
    path('morse/', include('morsecode.urls')),

    path('support/', views.render_support_page, name='supportPage'),

    path('api/v1/', include('apirelay.urls')),
]