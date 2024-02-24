from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET

from .models import Category
from .models import Topic


@require_GET
def category_list(request: HttpRequest):
    objs = Category.objects.all()
    return JsonResponse(data={"result": [{"id": obj.id, "name": obj.name, "slug": obj.slug} for obj in objs]})\


@require_GET
def topic_list(request: HttpRequest):
    objs = Topic.objects.all()
    return JsonResponse(data={"result": [{"id": obj.id, "title": obj.title, "slug": obj.slug} for obj in objs]})