from django.conf.urls import patterns, url
from article import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^(?P<articleID>\d)/$',views.single),
	
]