# Generated by Django 4.2.10 on 2024-02-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['category', 'date_created'], 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AddField(
            model_name='topic',
            name='is_published',
            field=models.BooleanField(db_index=True, default=False, help_text='Опубликован', verbose_name='опубликован'),
        ),
    ]
