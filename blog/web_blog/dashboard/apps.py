from django.conf.urls import url
from oscar.core.application import Application
from oscar.core.loading import get_class


class BlogDashboard(Application):
    name = 'blog-dashboard'

    blog_post_list_view = get_class('web_blog.dashboard.views', 'BlogPostListView')
    blog_post_detail_update_view = get_class('web_blog.dashboard.views', 'BlogPostDetailUpdateView')
    blog_post_detail_create_view = get_class('web_blog.dashboard.views', 'BlogPostDetailCreateView')

    def get_urls(self):
        urls = [
            url(r'^$',
                self.blog_post_list_view.as_view(), name='blog-post-list'),
            url(r'^update/detail/(?P<post_id>\d+)/$',
                self.blog_post_detail_update_view.as_view(), name='blog-post-detail'),
            url(r'^create/detail/$',
                self.blog_post_detail_create_view.as_view(), name='blog-post-create-detail'),
        ]
        return self.post_process_urls(urls)


application = BlogDashboard()
