"""
URL configuration for mmis_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include # Import include
from . import views # Import the project views

urlpatterns = [
    path("", views.home_view, name="home"), # Add this for the root URL
    path("dashboard/", views.protected_home_view, name="dashboard"), # Add this for the dashboard
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('hr/', include('hr_payroll.urls', namespace='hr_payroll')),
]
