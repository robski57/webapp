from django.conf.urls import include, url, patterns
from django.contrib import admin
#from.views.generic.simple import direct_to_template
from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.tweet, name='tweet'),
    #url(r'^$', views.photoapp, name='photoapp')
    
    
]
