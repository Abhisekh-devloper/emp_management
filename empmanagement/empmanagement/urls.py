"""
empmanagement URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts (Login / Register)
    path('', include('accounts.urls')),

    # Employee Management System
    path('ems/', include('employee.urls')),
]


# Serve Media Files (Profile Photos)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)