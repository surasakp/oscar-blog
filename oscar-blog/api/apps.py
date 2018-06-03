from rest_framework import routers
from rest_framework.authtoken import views
from oscar.core.application import Application

from django.conf.urls import url, include

from api.views import PostViewSet, CategoryViewSet, UserLoginViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, base_name='posts')
router.register(r'categories', CategoryViewSet, base_name='categories')


class Api(Application):
    name = 'api'

    def get_urls(self):
        urls = [
            url(r'^', include(router.urls)),
            url(r'^login/', UserLoginViewSet.as_view()),
            url(r'^api-token-auth/', views.obtain_auth_token),
            url(r'^categories/(?P<pk>[0-9]+)/blogs/$',
                PostViewSet.as_view({'get': 'category_blogs'}), name='category-blogs')
        ]

        return self.post_process_urls(urls)


application = Api()
