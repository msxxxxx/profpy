from .models import Category
from .models import Topic

from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET
from django.views.generic import *
from .forms import FeedbackForm, CategoryForm

@require_GET
def category_list(request: HttpRequest):
    objs = Category.objects.all()
    return JsonResponse(data={"result": [{"slug": obj.slug} for obj in objs]})


# @require_GET
# def topic_list(request: HttpRequest):
#     objs = Topic.objects.all()
#     data = [obj.id for obj in objs]
#     return data

class CategoryListView(ListView):
    model = Category
    queryset = model.objects.all()
    template_name = "blog/category_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get("q"):
            queryset = queryset.filter(name__icontains=self.request.GET.get("q"))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["title"] = "Category List"
        context["feedback_form"] = FeedbackForm()
        context["category_form"] = CategoryForm()
        return context

    def post(self, request: HttpRequest):
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            ...
        return self.get(request=request)


@require_GET
def topic_list(request: HttpRequest):
    objs = Topic.objects.all()
    return JsonResponse(data={"result": [{"id": obj.id, "title": obj.title, "slug": obj.slug} for obj in objs]})