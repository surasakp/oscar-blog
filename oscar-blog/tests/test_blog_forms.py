from oscar.core.loading import get_class

from django.test import TestCase

SearchPostForm = get_class('appblog.forms', 'SearchPostForm')


class TestSearchPostForm(TestCase):
    def setUp(self):
        self.form = SearchPostForm

    def test_search_post_form_should_have_expected_field(self):
        expected_field = ['search']
        self.assertEqual(self.form.Meta.fields, expected_field)
