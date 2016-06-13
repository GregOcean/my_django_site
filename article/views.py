from django.shortcuts import render_to_response

from django.http import HttpResponse
import datetime

from django.shortcuts import render_to_response
import MySQLdb
from article.models import Blog
def index(request):
	blog_list = Blog.objects.order_by('create_time')#need to changed
	context_dict = {'blogs':blog_list}
	return render_to_response('article/full-width.html',{'blogs':blog_list})

def single(request, articleID=None):
	single_blog = Blog.objects.get(id=articleID)
	#context_dict = {'blogs':blog_list}
	return render_to_response('article/single.html',{'blog':single_blog})
