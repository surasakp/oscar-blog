from oscar.core.loading import is_model_registered
from web_blog.abstract_models import AbstractCategory, AbstractPost, AbstractCategoryGroup


if not is_model_registered('web_blog', 'Category'):
    class Category(AbstractCategory):
        pass

if not is_model_registered('web_blog', 'Post'):
    class Post(AbstractPost):
        pass

if not is_model_registered('web_blog', 'CategoryGroup'):
    class CategoryGroup(AbstractCategoryGroup):
        pass
