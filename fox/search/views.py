from django.shortcuts import render
from django.db.models import Q
from blog.models import Blog
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(body__icontains=query)

            results= Blog.objects.filter(lookups).distinct()
            
            body={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search/search.html', body)

        else:
            return render(request, 'search/search.html')

    else:
        return render(request, 'search/search.html')
