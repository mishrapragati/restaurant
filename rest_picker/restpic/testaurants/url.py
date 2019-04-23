from django.conf.urls import patterns, url
from django.views.generic import ListView
from restaurants.models import Food
from django.conf import settings

urlpatterns = patterns('restaurants.views',
       url(r'^$',
           ListView.as_view(model=Food,
             template_name='restaurants/index.html'),
           name='index'),
       url(r'^food/(?P&lt;food_id&gt;\d+)/$',
           'choose_town',
           name='choose_town'),
       url(r'^food/(?P&lt;food_id&gt;\d+)/town/(?P&lt;town_id&gt;\d+)/$',
           'choose_restaurant',
           name='choose_restaurant'),
       url(r'^rest/(?P&lt;rest_id&gt;\d+)/$',
           'restaurant',
           name='restaurant'),
       url(r'^(?P&lt;rest_id&gt;\d+)/vote/$',
           'vote',
           name='vote'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
         (r'^media/(?P.*)$',
          'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}))