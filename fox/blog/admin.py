from django.contrib import admin
from .models import *
from django.utils.html import format_html


class BlogImageAdmin(admin.StackedInline):
    model = BlogImages
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    def blogImage(self,object):
        return format_html("<img src='{}' width='40'/>".format(object.image.url))
    inlines=[BlogImageAdmin]
    list_display = ('blogImage','title', 'slug','status','updated_on','pub_date')
    search_fields = ['title', 'body']
    pre_populated_fields = {'slug': ('title',)}
    list_display_links = ['blogImage', 'title']
    list_editable=['status',]

    class Meta:
        model=Blog

@admin.register(BlogView)
class BlogViewAdmin(admin.ModelAdmin):
    def blogImage(self,object):
        return format_html("<img src='{}' width='40'/>".format(object.blog.image.url))
    list_display = ('blogImage', 'blog', 'ip', 'created')
    list_filter=('blog',)
    list_display_links = ['blogImage', 'blog']

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
    def blogImage(self,object):
        return format_html("<img src='{}' width='40'/>".format(object.image.url))
    list_display = ('blogImage', 'blog', )
    list_filter = ( 'blog',)

@admin.register(FileUploader)
class FileUploaderAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_on')
    
@admin.register(HeaderBlogs)
class HeaderBlogsAdmin(admin.ModelAdmin):
    list_display = ('blog',)

