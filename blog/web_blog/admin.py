from django.contrib import admin

from oscar.core.loading import get_model


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'authour', 'post_date', 'created_at', 'updated_at')
    search_fields = ('title', 'authour__username')
    list_filter = ['post_date']


# Register your models here.
Category = get_model('web_blog', 'Category')
Post = get_model('web_blog', 'Post')
CategoryGroup = get_model('web_blog', 'CategoryGroup')
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(CategoryGroup)
