"""
URL configuration for career_counseling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('assessment.urls')),  # Include your backend API routes
    re_path(r'^manifest.json$', TemplateView.as_view(template_name="manifest.json", content_type="application/json")),
    path('favicon.ico', serve, {'path': 'favicon.ico', 'document_root': settings.STATICFILES_DIRS[0]}),  # Serve favicon
    # Route for serving the React frontend
    path('', TemplateView.as_view(template_name='index.html')),  # Serve the main entry point of React
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
