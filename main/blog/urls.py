from django.urls import path

# from blog.views import category_list, category_detail
from .views import *
from django.urls import path
from .views import category_list

# urlpatterns = [
#     # path("api/v1/categories/<int:pk>/", category_detail),
#     # path("api/v1/categories/", category_list,)
#     # path("categories/<slug:slug>/", CategoryDetailView.as_view()),
#     #path("categories/", CategoryListView.as_view())
#     #path("contact/", ContactFormView.as_view(), name="contact"),
#     #path("<slug:slug>/", TopicDetailView.as_view(), name="topic_detail"),
#     path("/", TopicListView.as_view(), name="index"),
# ]
urlpatterns = [
    path("api/v1/categories/", category_list),
    path("api/v1/posts/", topic_list)
]