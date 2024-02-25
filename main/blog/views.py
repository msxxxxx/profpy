from django.urls import reverse_lazy
from django.views.generic import *
from django.core.mail import send_mail

from .forms import FeedbackForm
from .models import Topic

from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET


class TopicListView(ListView):
    model = Topic
    template_name = "blog/index.html"
    paginate_by = 5
    extra_context = {
        "heading": "Main Page",
        "header_image": 'blog/assets/img/home-bg.jpg'
    }


class TopicDetailView(DetailView):
    model = Topic
    template_name = "blog/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = context.get("topic").title
        context["header_image"] = "blog/assets/img/post-sample-image.jpg"
        return context


class ContactFormView(FormView):
    template_name = "blog/contact.html"
    extra_context = {
        "heading": "Contact Page",
        "header_image": 'blog/assets/img/home-bg.jpg'
    }
    form_class = FeedbackForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form: FeedbackForm):
        # send_mail(
        #     subject="Feedback",
        #     message=form.data.get("message"),
        #     from_email=None,
        #     recipient_list=[form.data.get("email")]
        # )
        print(form.data)
        # return self.get(request=)
        return super().form_valid(form=form)

    # def post(self, request: HttpRequest):
    #     form = FeedbackForm(data=request.POST)
    #     if form.is_valid():
    #         # form.save()
    #         print(form.data)
    #     return self.get(request=request)

# from .models import Category
# from .models import Topic
#
# from django.http import HttpRequest, JsonResponse
# from django.views.decorators.http import require_GET
# from django.views.generic import *
# # from django.shortcuts import *
# from .forms import FeedbackForm, CategoryForm
#
# @require_GET
# def category_list(request: HttpRequest):
#     objs = Category.objects.all()
#     return JsonResponse(data={"result": [{"slug": obj.slug} for obj in objs]})
#
#
# # @require_GET
# # def topic_list(request: HttpRequest):
# #     objs = Topic.objects.all()
# #     data = [obj.id for obj in objs]
# #     return data
#
# class CategoryListView(ListView):
#     model = Category
#     queryset = model.objects.all()
#     template_name = "blog/category_list.html"
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if self.request.GET.get("q"):
#             queryset = queryset.filter(name__icontains=self.request.GET.get("q"))
#         return queryset
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context["title"] = "Category List"
#         context["feedback_form"] = FeedbackForm()
#         context["category_form"] = CategoryForm()
#         return context
#
#     def post(self, request: HttpRequest):
#         form = CategoryForm(data=request.POST)
#         # form = FeedbackForm(data=request.POST)
#         if form.is_valid():
#             # form.save()
#             print(form.data)
#         return self.get(request=request)
#
#
# class CategoryDetailView(DetailView):
#     model = Category
#     template_name = "blog/category_detail.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context)
#         return context
#
# @require_GET
# def topic_list(request: HttpRequest):
#     objs = Topic.objects.all()
#     return JsonResponse(data={"result": [{"id": obj.id, "title": obj.title, "slug": obj.slug} for obj in objs]})