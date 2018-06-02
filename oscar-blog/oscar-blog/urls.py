"""blog URL Configuration

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
from oscar.app import application

from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from appblog.dashboard.apps import application as dashboard_blogs_app
from appblog.apps import application as blogs_app
from api.apps import application as api_app

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(application.urls)),
    url(r'^dashboard/blogs/', include(dashboard_blogs_app.urls)),
    url(r'^blogs/', include(blogs_app.urls)),
    url(r'^api/', include(api_app.urls))
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
