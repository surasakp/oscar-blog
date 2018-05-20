import factory
import datetime

from oscar.core.loading import get_model

from oscar.core.compat import get_user_model

__all__ = ['PostFactory', 'CategoryFactory', 'CategoryGroupFactory', 'UserFactory']


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user nummer %d' % n)
    email = factory.Sequence(lambda n: 'example_user_%s@example.com' % n)
    first_name = 'wade'
    last_name = 'wilson'
    password = factory.PostGenerationMethodCall('set_password', 'skelebrain')
    is_staff = True

    class Meta:
        model = get_user_model()


class PostFactory(factory.DjangoModelFactory):
    title = 'title post'
    content = 'content post'
    post_date = datetime.datetime.now()
    excerpt = 'excerpt post'
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = get_model('appblog', 'Post')


class CategoryFactory(factory.DjangoModelFactory):
    name = 'Test Category'

    class Meta:
        model = get_model('appblog', 'Category')


class CategoryGroupFactory(factory.DjangoModelFactory):
    post = PostFactory
    category = CategoryFactory
    group = 'group1'

    class Meta:
        model = get_model('appblog', 'CategoryGroup')
