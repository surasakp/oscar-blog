from django.db import models

from oscar.core.compat import AUTH_USER_MODEL
from .mixins import Timestamp
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class AbstractCategory(Timestamp):
    name = models.CharField(max_length=200)

    def __str__(self):
        return 'name : ' + self.name


class AbstractPost(Timestamp):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    featured_image = models.ImageField(
        _("Featured Image"),
        upload_to=settings.OSCAR_IMAGE_FOLDER, max_length=255)
    post_date = models.DateField('date post')
    authour = models.ForeignKey(
        AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE)
    category = models.ManyToManyField(
        AbstractCategory,
        blank=True,
        through='AbstractCategoryGroup',
        verbose_name=_("Category")
    )
    excerpt = models.CharField(max_length=1000)

    def __str__(self):
        return 'title : ' + self.title


class AbstractCategoryGroup(Timestamp):
    post = models.ForeignKey(AbstractPost, on_delete=models.CASCADE)
    catagory = models.ForeignKey(AbstractCategory, on_delete=models.CASCADE)
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.group
