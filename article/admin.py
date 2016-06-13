from django.contrib import admin
# Register your models here.
from article.models import *
class Blog_admin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/tiny_mce/tiny_mce.js',
            '/static/js/textareas.js',
     )
admin.site.register(Blog, Blog_admin)
admin.site.register(Classification)
admin.site.register(Tag)
#admin.site.register(Blog_admin)
#admin.site.register(Blog)