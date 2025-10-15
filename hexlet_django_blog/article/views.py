# from django.shortcuts import render
from django.views.generic.base import TemplateView


# def index(request):
#     return HttpResponse("article")
# Create your views here.

# def index(request):
#     app_name = 'article'
#     return render(
#         request,
#         "articles/index.html",
#         context={
#             "app_name": app_name,
#         },
#     )

class index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = 'article'
        return context
