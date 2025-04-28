from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_context = {
        "page_title" : "Hi Ishan Singh",
        "page_visit_count":page_qs.count(),
        "total_visit_count": qs.count()
    }
    
    path=request.path
    print("Path", path)
    PageVisit.objects.create(path=request.path)
    return render(request,"home.html",my_context)

