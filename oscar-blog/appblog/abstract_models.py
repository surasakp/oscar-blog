from oscar.core.compat import AUTH_USER_MODEL

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.


class Timestamp(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractCategory(Timestamp):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AbstractPost(Timestamp):

    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    featured_image = models.ImageField(_("Featured Image"), upload_to=settings.OSCAR_IMAGE_FOLDER)
    post_date = models.DateField(default=timezone.now)
    authour = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    category = models.ManyToManyField(
        AbstractCategory, blank=True, through='AbstractCategoryGroup', verbose_name=_("Category"))
    excerpt = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class AbstractCategoryGroup(Timestamp):
    post = models.ForeignKey(AbstractPost, on_delete=models.CASCADE)
    catagory = models.ForeignKey(AbstractCategory, on_delete=models.CASCADE)
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.group
