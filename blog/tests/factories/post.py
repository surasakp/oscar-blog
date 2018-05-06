import factory
from oscar.core.loading import get_model
import datetime

__all__ = ['PostFactory']


class PostFactory(factory.DjangoModelFactory):
    title = 'test_post'
    content = 'test_content'
    post_date = datetime.datetime.now()
    excerpt = 'test_excerpt'

    class Meta:
        model = get_model('web_blog', 'Post')
