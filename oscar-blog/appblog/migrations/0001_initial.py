# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-07 13:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AbstractCategoryGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AbstractPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=2000)),
                ('featured_image', models.ImageField(upload_to='images/products/%Y/%m/', verbose_name='Featured Image')),
                ('post_date', models.DateField(default=django.utils.timezone.now)),
                ('excerpt', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('abstractcategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appblog.AbstractCategory')),
            ],
            options={
                'abstract': False,
            },
            bases=('appblog.abstractcategory',),
        ),
        migrations.CreateModel(
            name='CategoryGroup',
            fields=[
                ('abstractcategorygroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appblog.AbstractCategoryGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=('appblog.abstractcategorygroup',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('abstractpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appblog.AbstractPost')),
            ],
            options={
                'abstract': False,
            },
            bases=('appblog.abstractpost',),
        ),
        migrations.AddField(
            model_name='abstractpost',
            name='authour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractpost',
            name='category',
            field=models.ManyToManyField(blank=True, through='appblog.AbstractCategoryGroup', to='appblog.AbstractCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='abstractcategorygroup',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appblog.AbstractCategory'),
        ),
        migrations.AddField(
            model_name='abstractcategorygroup',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appblog.AbstractPost'),
        ),
    ]