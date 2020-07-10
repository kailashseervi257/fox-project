from django.contrib import admin

from .models import Blog, BlogView

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','updated_on','pub_date')
    search_fields = ['title', 'body']
    pre_populated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogView)
