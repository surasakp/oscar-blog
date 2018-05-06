from django.conf.urls import include, url
# from .views import index
from web_blog.dashboard.apps import application as blog_dashboard_application

urlpatterns = [
    url(r'^post/', include(blog_dashboard_application.urls))
]
