from django.contrib import admin

# Register your models here.

from .models import Category, Topic


@admin.action(description="Опубликовать")
def make_published(modeladmin, request, queryset):  # noqa
    for item in queryset:
        item.is_published = True
        item.save()


@admin.action(description="Снять с публикации")
def make_unpublished(modeladmin, request, queryset):  # noqa
    for item in queryset:
        item.is_published = False
        item.save()

class TopicInline(admin.StackedInline):
    model = Topic
    verbose_name = "post"
    verbose_name_plural = "posts"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published")
    date_hierarchy = "date_created"
    prepopulated_fields = {
        "slug": ("title", )
    }
    list_filter = ("category", "is_published")
    preserve_filters = False
    actions = (make_published, make_unpublished)
