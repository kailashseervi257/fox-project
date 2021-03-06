from django.shortcuts import render,get_object_or_404
from .models import Blog, BlogView, BlogImages
from django.http.response import HttpResponse
from itertools import chain
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .forms import CommentForm

# ---class based
# class BlogList(generic.ListView):
#     queryset = Blog.objects.filter(status=1).order_by('-pub_date')
#     template_name = 'blog-home.html'
#     paginate_by = 3

# class BlogDetail(generic.DetailView):
#     model = Blog
#     template_name='details.html'

#---------------
def blog(request):
    blogs = Blog.objects.filter(status=1).order_by('pub_date').reverse()
    paginator = Paginator(blogs, 9)
    page_number = request.GET.get('page')
    try:
        blog_list = paginator.page(page_number)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog-home.html', {'blogs':blogs,'page':page_number,'blog_list': blog_list})
    

def detail(request, slug):
    singleBlog = get_object_or_404(Blog, slug=slug)
    photos=BlogImages.objects.filter(blog=singleBlog)
    comments = singleBlog.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = singleBlog
            new_comment.save()
    else:
        comment_form = CommentForm()

    resultQuerySet = Blog.objects.order_by('views_total').reverse().filter(status=1)[:5]
    if singleBlog:
        record_view(request, slug)
        return render(request, 'blog/details.html', {'singleBlog': singleBlog,
                                                    'popularBlogs': resultQuerySet,
                                                    'comments': comments,
                                                    'new_comment': new_comment,
                                                    'comment_form': comment_form,
                                                    'photos':photos,})

def record_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if not BlogView.objects.filter(
        blog=blog,
        session=request.session.session_key):
        view=BlogView(blog=blog,
        ip=request.session.session_key,
        session=request.session.session_key)
        blog.views_total += 1
        blog.save()
        view.save()
    return HttpResponse(BlogView.objects.filter(blog=blog).count())


def category(request,cat):
    query = cat
    if query is not None:
        submitbutton = 'cat'
        results = Blog.objects.filter(status=1, category=query).order_by('pub_date').reverse()
        if results is not None:
            body={'results': results, 'submitbutton':submitbutton,'query':query}
            return render(request, 'search/search.html', body)
    else:
        return render(request, 'search/search.html')
