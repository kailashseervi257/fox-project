from django.contrib import admin

from .models import Blog, BlogView, Comment, BlogImages, FileUploader


class BlogImageAdmin(admin.StackedInline):
    model = BlogImages
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines=[BlogImageAdmin]
    list_display = ('title', 'slug', 'status','updated_on','pub_date')
    search_fields = ['title', 'body']
    pre_populated_fields = {'slug': ('title',)}

    class Meta:
        model=Blog

@admin.register(BlogView)
class BlogViewAdmin(admin.ModelAdmin):
    list_display = ('blog_id', 'blog', 'ip', 'created')
    list_filter=('blog',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on','blog')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments','disapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
    
    def disapprove_comments(self, request, queryset):
        queryset.update(active=False)

@admin.register(BlogImages)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'blog', )
    list_filter = ( 'blog',)

@admin.register(FileUploader)
class FileUploaderAdmin(admin.ModelAdmin):
    list_display=('file', 'uploaded_on')