
from django.conf.urls import *
from django.contrib import admin
from my_django_site.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
	url(r'^$',homepage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^home/$',homepage),
    #url(r'^comments/',include('django.contrib.comments.urls')),
    url(r'^about/$', about),
    url(r'^contact/$', contact),
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',),  
    url(r'^article/', include('article.urls')), # ADD THIS NEW TUPLE!
    url(r'^class/(?P<class_id>\d)/',class_filter),
    url(r'^tag/(?P<tag_id>\d)',tag_filter),

    #url(r'^generic-detail-view-ajax/(?P<pk>\d+)/$',
    #    views.PostDetailJSONView.as_view(),
    #    name="ajax"),
    #url(r'^hitcount-detail-view/(?P<pk>\d+)/$',
    #    views.PostDetailView.as_view(),
    #    name="detail"),
    #url(r'^hitcount-detail-view-count-hit/(?P<pk>\d+)/$',
     #   views.PostCountHitDetailView.as_view(),
     #   name="detail-with-count"),

    # for our built-in ajax post view
    #url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_PATH)
#urlpatterns += staticfiles_urlpatterns()