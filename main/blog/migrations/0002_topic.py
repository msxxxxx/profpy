# Generated by Django 4.2.10 on 2024-02-13 17:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title post', max_length=128, validators=[django.core.validators.MinLengthValidator(limit_value=2)], verbose_name='title')),
                ('body', models.TextField(help_text='Text post', max_length=128, validators=[django.core.validators.MinLengthValidator(limit_value=2)], verbose_name='test')),
                ('slug', models.SlugField(help_text='URL', max_length=128, validators=[django.core.validators.MinLengthValidator(limit_value=2)], verbose_name='url')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date create')),
                ('category', models.ForeignKey(help_text='category post', on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='category')),
            ],
            options={
                'verbose_name': ('post',),
                'verbose_name_plural': ('posts',),
                'ordering': ['category', 'date_created'],
            },
        ),
    ]