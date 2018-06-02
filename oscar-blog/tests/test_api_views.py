import datetime
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from .factories.blogs import CategoryFactory, PostFactory, CategoryGroupFactory
from appblog.models import Post, Category
from .util import Util
from api.serializers import PostSerializer, CategorySerializer
from api.views import PostViewSet

util = Util()


class TestViewDefaultRouter(APITestCase):

    def test_view_default_router_should_display_expected_apis(self):
        expected_apis = {'posts': 'http://testserver/api/posts/', 'categories': 'http://testserver/api/categories/'}
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_apis)


class TestViewPostList(APITestCase):

    username = 'admin'
    password = 'top12345'

    def login(self):

        self.user = User.objects.create(username=self.username)
        self.user.set_password(self.password)
        self.user.is_staff = True
        self.user.save()

        self.client.login(
            username=self.username,
            password=self.password
        )
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.user.auth_token))

    def setUp(self):
        upload_file = util.create_image()
        self.category_factory = CategoryFactory()
        self.post_factory = PostFactory(featured_image=SimpleUploadedFile(upload_file.name, upload_file.read()))
        CategoryGroupFactory(category=self.category_factory, post=self.post_factory)

    def test_entrance_view_post_with_not_login_should_have_validate_authentication(self):
        url_view_post_list = reverse('api:posts-list')
        response_list = self.client.get(url_view_post_list)
        self.assertEqual(response_list.status_code, 403)

        url_view_post_detail = reverse('api:posts-detail', kwargs={'pk': self.post_factory.id})
        response_detail = self.client.get(url_view_post_detail)
        self.assertEqual(response_detail.status_code, 403)

    def test_api_get_view_post_list_should_have_expected_data(self):

        self.login()
        url_view_post_list = reverse('api:posts-list')
        response = self.client.get(url_view_post_list)
        self.assertEqual(response.status_code, 200)

        factory = APIRequestFactory()
        request = factory.get(url_view_post_list)

        serializer_context = {
            'request': request,
        }

        post_set = Post.objects.all()
        serializer = PostSerializer(post_set, many=True, context=serializer_context)
        self.assertEqual(response.data, serializer.data)

    def test_api_get_view_post_detail_should_have_expect_data(self):

        self.login()
        url_view_post_detail = reverse('api:posts-detail', kwargs={'pk': self.post_factory.id})
        response = self.client.get(url_view_post_detail)
        self.assertEqual(response.status_code, 200)

        factory = APIRequestFactory()
        request = factory.get(url_view_post_detail)

        serializer_context = {
            'request': request,
        }

        post = Post.objects.get(id=self.post_factory.id)
        serializer = PostSerializer(instance=post, many=False, context=serializer_context)
        self.assertEqual(response.data, serializer.data)

    def test_api_post_view_post_list_should_have_expected_data_in_db(self):

        self.login()
        url_view_post_list = reverse('api:posts-list')
        upload_file = util.create_image()
        data = {
            'title': 'title api post',
            'content': 'content api post',
            'featured_image': SimpleUploadedFile(upload_file.name, upload_file.read()),
            'post_date': datetime.date(2018, 5, 30),
            'author': self.user.id,
            'category': [
                reverse('api:category-blogs', kwargs={'pk': self.category_factory.id})
            ],
            'excerpt': 'excerpt api post'
        }

        factory = APIRequestFactory()
        request = factory.post(url_view_post_list, data, format='multipart')

        force_authenticate(request, user=self.user, token=self.user.auth_token)
        view = PostViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, 201)

        post = Post.objects.get(id=response.data['id'])
        self.assertEqual(post.title, data['title'])
        self.assertEqual(post.content, data['content'])
        self.assertEqual(post.excerpt, data['excerpt'])

    def test_api_put_view_post_detail_should_have_expected_data_in_db(self):

        self.login()
        url_view_post_detail = reverse('api:posts-detail', kwargs={'pk': self.post_factory.id})

        upload_file = util.create_image()
        data = {
            'title': 'title api put',
            'content': 'content api put',
            'featured_image': SimpleUploadedFile(upload_file.name, upload_file.read()),
            'post_date': datetime.date(2018, 6, 30),
            'author': self.user.id,
            'category': [
                reverse('api:category-blogs', kwargs={'pk': self.category_factory.id})
            ],
            'excerpt': 'excerpt api put'
        }

        response = self.client.put(url_view_post_detail, data, format='multipart')
        self.assertEqual(response.status_code, 200)

        post = Post.objects.get(id=self.post_factory.id)
        self.assertEqual(post.title, data['title'])
        self.assertEqual(post.content, data['content'])
        self.assertEqual(post.excerpt, data['excerpt'])


class TestViewCategoryList(APITestCase):

    username = 'admin'
    password = 'top12345'

    def login(self):
        self.user = User.objects.create(username=self.username)
        self.user.set_password(self.password)
        self.user.is_staff = True
        self.user.save()
        self.client.login(
            username=self.username,
            password=self.password
        )
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.user.auth_token))

    def setUp(self):
        self.category_factory = CategoryFactory()
        CategoryFactory(name='Test Category2')
        CategoryFactory(name='Test Category3')

    def test_entrance_view_category_with_not_login_should_have_validate_authentication(self):
        url_view_category_list = reverse('api:categories-list')
        response_list = self.client.get(url_view_category_list)
        self.assertEqual(response_list.status_code, 403)

        url_view_category_detail = reverse('api:categories-detail', kwargs={'pk': self.category_factory.id})
        response_detail = self.client.get(url_view_category_detail)
        self.assertEqual(response_detail.status_code, 403)

    def test_view_category_list_should_have_expected_data(self):

        self.login()
        url_view_category_list = reverse('api:categories-list')
        response = self.client.get(url_view_category_list)
        self.assertEqual(response.status_code, 200)

        factory = APIRequestFactory()
        request = factory.get(url_view_category_list)

        serializer_context = {
            'request': request,
        }

        category_set = Category.objects.all()
        serializer = CategorySerializer(category_set, many=True, context=serializer_context)
        self.assertEqual(response.data, serializer.data)

    def test_api_post_view_category_list_should_have_expected_data_in_db(self):

        self.login()
        url_view_categories_list = reverse('api:categories-list')
        data = {
            'name': 'name category api post',
        }

        response = self.client.post(url_view_categories_list, data, format='json')
        self.assertEqual(response.status_code, 201)
        category = Category.objects.get(id=response.data['id'])
        self.assertEqual(category.name, data['name'])

    def test_api_put_view_category_detail_should_have_expected_data_in_db(self):

        self.login()
        url_view_categories_detail = reverse('api:categories-detail', kwargs={'pk': self.category_factory.id})
        data = {
            'name': 'name category api put',
        }

        response = self.client.put(url_view_categories_detail, data, format='json')
        self.assertEqual(response.status_code, 200)

        category = Category.objects.get(id=self.category_factory.id)
        self.assertEqual(category.name, data['name'])
