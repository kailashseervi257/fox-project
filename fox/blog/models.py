from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from ckeditor_uploader.fields import RichTextUploadingField
import pytz
IST=pytz.timezone('Asia/Kolkata')
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

Mtech = 'Mtech'
MBA = 'MBA'
UGMedical = 'UG-Medical'
PGMedical = 'PG-Medical'
Engineering = 'Engineering'
Commerce = 'Commerce'
Law = 'Law'
Architecture = 'Architecture'
Management = 'Management'
All='All'
Arts='Arts'
Updates = 'Updates'
CATEGORY = (
    (Mtech, 'Mtech'),
    (MBA, 'MBA'),
    (UGMedical, 'UG-Medical'),
    (PGMedical, 'PG-Medical'),
    (Engineering, 'Engineering'),
    (Commerce, 'Commerce'),
    (Law, 'Law'),
    (Architecture, 'Architecture'),
    (Management, 'Management'),
    (All,'All'),
    (Arts,'Arts'),
    (Updates,'Updates'),
)

class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255,default=None)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True)
    body = RichTextUploadingField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', default=1)
    views_total = models.IntegerField(default=1)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    category=models.CharField(max_length=255,choices=CATEGORY, default=All)
    
    class Meta:
        ordering = ['-pub_date']
        

    def __str__(self):
        return self.title

    def pub_date_pro_day(self):
        return self.pub_date.strftime('%e')
    
    def pub_date_pro_month(self):
        return self.pub_date.strftime('%b')
    
    def pub_date_pro_year(self):
        return self.pub_date.strftime('%Y')
    
    def pub_date_pro(self):
        return self.pub_date.strftime('%e %b %Y')
    
    def pubdatepro(self):
        return self.updated_on.strftime('%e %b %Y')
    
    def short(self):
        return self.body[:62]


class BlogImages(models.Model):
    blog = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return "{}'s image {}".format(self.blog.title, self.image)
    

class BlogView(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    ip=models.CharField(max_length=40,blank=True, default='',null=True)
    session=models.CharField(max_length=40, blank=True, default='',null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.blog.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class FileUploader(models.Model):
    file = models.FileField(upload_to='files/')
    description=models.CharField(max_length=255, default='File')
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}'s file".format(self.file)

class HeaderBlogs(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.blog)
