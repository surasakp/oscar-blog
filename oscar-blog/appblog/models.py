from oscar.core.loading import is_model_registered
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
