__author__ = 'trueutkarsh'


from django.conf.urls import patterns, include, url
from database import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'netyap.views.sample-app', name='sample-app'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.getdata, name='getdata'),
    #url(r'^thanks', views.thanks, name='thanks'),
)
