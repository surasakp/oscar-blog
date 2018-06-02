from oscar.core.loading import is_model_registered
from rest_framework.authtoken.models import Token

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from appblog.abstract_models import AbstractCategory, AbstractPost, AbstractCategoryGroup


if not is_model_registered('appblog', 'Category'):
    class Category(AbstractCategory):
        pass

if not is_model_registered('appblog', 'Post'):
    class Post(AbstractPost):
        pass

if not is_model_registered('appblog', 'CategoryGroup'):
    class CategoryGroup(AbstractCategoryGroup):
        pass


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
