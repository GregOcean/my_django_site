from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from article.models import *
import datetime
from django.utils import timezone
import MySQLdb

#from __future__ import unicode_literals
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import DetailView, TemplateView
from hitcount.views import HitCountDetailView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def homepage(request):
	#blog_list = Blog.objects.order_by('-create_time')
	category_list = Classification.objects.order_by('id')
	tag_list = Tag.objects.order_by('id')
	recent_list = Blog.objects.filter(create_time__isnull=False).order_by('-create_time')[:5]
    #recent_list = blog.objects.filter(published_date__range=(start_date, end_date))
	#recent_list = Blog.objects.filter(create_time=time_point)
	blogs = Blog.objects.order_by('-create_time')
	paginator=Paginator(blogs,2)
	page=request.GET.get('page')
	try:
		blog_list = paginator.page(page)
	except PageNotAnInteger:
		blog_list = paginator.page(1)
	except EmptyPage:
		blog_list = paginator.page(paginator.num_pages)

	context_dict = {'blogs':blog_list, 'tags':tag_list, 'categories':category_list, 'recent_blogs':recent_list}
	return render_to_response('index.html',context_dict)

def about(request):
	return render_to_response('about.html',RequestContext(request))

def contact(request):
	return render_to_response('contact.html',RequestContext(request))

def class_filter(request, class_id=None):
	category_list = Classification.objects.order_by('id')
	tag_list = Tag.objects.order_by('id')
	blog_class_list = Blog.objects.filter(classification_id=class_id).order_by('-create_time')	
	recent_list = Blog.objects.filter(create_time__isnull=False).order_by('-create_time')[:5]

	paginator=Paginator(blog_class_list,2)
	page=request.GET.get('page')
	try:
		blog_list = paginator.page(page)
	except PageNotAnInteger:
		blog_list = paginator.page(1)
	except EmptyPage:
		blog_list = paginator.page(paginator.num_pages)

	context_dict = {'blogs':blog_list, 'tags':tag_list, 'categories':category_list, 'recent_blogs':recent_list}
	
	return render_to_response('index.html',context_dict)

def tag_filter(request, tag_id=None):
	category_list = Classification.objects.order_by('id')	
	tag_list = Tag.objects.order_by('id')
	#blog_class_list = Blog.objects.filter(classification_id=class_id)
	recent_list = Blog.objects.filter(create_time__isnull=False).order_by('-create_time')[:5]
	blog_tag_list = Blog.objects.all().filter(tags= tag_id).order_by('-create_time')

	paginator=Paginator(blog_tag_list,2)
	page=request.GET.get('page')
	try:
		blog_list = paginator.page(page)
	except PageNotAnInteger:
		blog_list = paginator.page(1)
	except EmptyPage:
		blog_list = paginator.page(paginator.num_pages)

	context_dict = {'blogs':blog_list, 'tags':tag_list, 'categories':category_list, 'recent_blogs':recent_list}
	
	return render_to_response('index.html',context_dict)