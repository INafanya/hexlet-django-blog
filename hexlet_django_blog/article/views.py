from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("article")
# Create your views here.

def index(request):
    app_name = 'article'
    return render(
        request,
        "articles/index.html",
        context={
            "app_name": app_name,
        },
    )
