from django.db import models
from django.core import validators
from django.utils.timezone import now
from typing import TYPE_CHECKING
from datetime import datetime

# Create your models here.

#blog_category
class Category(models.Model):
    if TYPE_CHECKING:
        name: str
        slug: str
    else:
        name = models.CharField(
            max_length=32,
            null=False,
            blank=False,
            unique=True,
            help_text="Name category",
            verbose_name="name", #lowcase prefer
            validators=[
                validators.MinLengthValidator(limit_value=2)
            ]
        )
        slug = models.SlugField(
            max_length=32,
            null=False,
            blank=False,
            unique=True,
            help_text="Link",
            verbose_name="link",
            validators=[
                validators.MinLengthValidator(limit_value=2)
            ]
        )

    def __str__(self) -> str:
        return self.name  # noqa

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "category"
        # abstract = True
        # managed = False
        # ordering = ["name"]
        # db_table = "blog_category"
        # db_table_comment = "Topics Category"


class Topic(models.Model):
    if TYPE_CHECKING:
        title: str
        body: str
        slug: str
        date_created: datetime
        category: Category
        category_id: int
        is_published: bool
    else:
        title = models.CharField(
            max_length=128,
            null=False,
            blank=False,
            help_text="Title post",
            verbose_name="title",
            validators=[
                validators.MinLengthValidator(limit_value=2)
            ]
        )
        body = models.TextField(
            max_length=128,
            null=False,
            blank=False,
            help_text="Text post",
            verbose_name="test",
            validators=[
                validators.MinLengthValidator(limit_value=2)
            ]
        )
        slug = models.SlugField(
            max_length=128,
            null=False,
            blank=False,
            help_text="URL",
            verbose_name="url",
            validators=[
                validators.MinLengthValidator(limit_value=2)
            ]
        )
        date_created = models.DateTimeField(
            verbose_name="date create",
            default=now
        )
        category = models.ForeignKey(
            to="Category",
            on_delete=models.PROTECT,
            verbose_name="category",
            help_text="category post"
        )
        is_published = models.BooleanField(
            default=False,
            verbose_name="опубликован",
            help_text="Опубликован",
            null=False,
            blank=False,
            db_index=True
        )

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["category", "date_created"]
        # indexes = [
        #     models.Index(fields=["category"])
        # ]
