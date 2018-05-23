from oscar.core.loading import get_class
from oscar.core.application import Application

from django.conf.urls import url


class AppBlog(Application):
    name = 'appblog'

    blog_post_index_view = get_class('appblog.views', 'BlogPostView')
    blog_post_detail_view = get_class('appblog.views', 'BlogPostDetailView')
    blog_category_view = get_class('appblog.views', 'BlogCategoryView')

    def get_urls(self):
        urls = [
            url(r'^posts/', self.blog_post_index_view.as_view(), name='posts-index-view'),
            url(r'^category/(?P<slug>[\w-]+)/$', self.blog_category_view.as_view(), name='category-view'),
            url(r'^post/detail/(?P<slug>[\w-]+)/$', self.blog_post_detail_view.as_view(), name='post-detail-view'),
        ]

        return self.post_process_urls(urls)


application = AppBlog()
