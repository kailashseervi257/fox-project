from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    views_total = models.IntegerField(default=19)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-pub_date']
    
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


class BlogView(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    ip=models.CharField(max_length=40)
    session=models.CharField(max_length=40)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.ip


