from django.shortcuts import render

def courses(request):
    return render(request,'course/course-home.html')
