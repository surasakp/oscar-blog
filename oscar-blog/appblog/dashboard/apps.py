from oscar.core.application import Application
from oscar.core.loading import get_class

from django.conf.urls import url


class BlogDashboard(Application):
    name = 'blog-dashboard'

    blog_post_list_view = get_class('appblog.dashboard.views', 'BlogPostListView')
    blog_post_detail_update_view = get_class('appblog.dashboard.views', 'BlogPostDetailUpdateView')
    blog_post_detail_create_view = get_class('appblog.dashboard.views', 'BlogPostDetailCreateView')
    blog_post_detail_delete_view = get_class('appblog.dashboard.views', 'BlogPostDetailDeleteView')

    blog_category_list_view = get_class('appblog.dashboard.views', 'BlogCetagoryListView')

    def get_urls(self):
        urls = [
            url(r'^post/$',
                self.blog_post_list_view.as_view(), name='blog-post-list'),
            url(r'^post/update/detail/(?P<id>\d+)/$',
                self.blog_post_detail_update_view.as_view(), name='blog-post-detail'),
            url(r'^post/create/detail/$',
                self.blog_post_detail_create_view.as_view(), name='blog-post-create-detail'),
            url(r'^post/delete/(?P<pk>\d+)/$',
                self.blog_post_detail_delete_view.as_view(), name='blog-post-delete-detail'),

            url(r'^category/$', self.blog_category_list_view.as_view(), name='blog-category-list')
        ]
        return self.post_process_urls(urls)


application = BlogDashboard()
