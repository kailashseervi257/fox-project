from django.contrib import admin

from .models import Blog, BlogView, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','updated_on','pub_date')
    search_fields = ['title', 'body']
    pre_populated_fields = {'slug': ('title',)}

class BlogViewAdmin(admin.ModelAdmin):
    list_display = ('blog_id', 'blog', 'ip', 'created')
    list_filter=('blog',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


    
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogView, BlogViewAdmin)
