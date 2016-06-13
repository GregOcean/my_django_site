#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from tinymce import models as tinymce_models

from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin
# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
            
    def __unicode__(self):
        return self.tag_name
            
class Classification(models.Model):
    name = models.CharField(max_length=20)
            
    def __unicode__(self):
        return self.name

class Blog(models.Model):
	title = models.CharField(max_length = 100, verbose_name='标题', null=False)
	content = models.TextField(verbose_name='内容', default='')#models.TextField()
	clicked = models.IntegerField(default=0, verbose_name='点击量', blank=True)
	create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
	update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
	summary = models.TextField(max_length=256, verbose_name='概述', default='')
	classification = models.ForeignKey(Classification,verbose_name='分类')
 	tags = models.ManyToManyField(Tag, blank=True,verbose_name='标签')
	
    #hit_count_generic = GenericRelation(
    #    HitCount, object_id_field='object_pk',
    #    related_query_name='hit_count_generic_relation')

	def __unicode__(self):
		return self.title

