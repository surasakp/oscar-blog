from oscar.core.loading import get_model

from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'authour', 'post_date', 'created_at', 'updated_at')
    search_fields = ('title', 'authour__username')
    list_filter = ['post_date']


# Register your models here.
Category = get_model('appblog', 'Category')
Post = get_model('appblog', 'Post')
CategoryGroup = get_model('appblog', 'CategoryGroup')
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(CategoryGroup)
