from django.test import TestCase
from oscar.core.loading import get_model, get_class


Post = get_model('appblog', 'Post')
PostForm = get_class('appblog.dashboard.forms', 'PostForm')


class TestDashboardPostForm(TestCase):
    def setUp(self):
        self.form = PostForm

    def test_should_have_fields_that_we_expect(self):
        expected_fields = ['title', 'content', 'featured_image', 'post_date', 'authour', 'excerpt']
        self.assertEquals(expected_fields, self.form.Meta.fields)

    def test_required_field_have_not_data(self):
        data = {}

        form = self.form(data=data)
        self.assertFalse(form.is_valid())

        expected_errors = {
            'title': ['This field is required.'],
            'content': ['This field is required.'],
            'featured_image': ['This field is required.'],
            'post_date': ['This field is required.'],
            'authour': ['This field is required.'],
            'excerpt': ['This field is required.']
        }

        self.assertDictEqual(form.errors, expected_errors)
