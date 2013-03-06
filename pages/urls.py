from django.conf.urls import patterns, url


urlpatterns = patterns('',
     url(r'^pages/$', 'pages.views.all_pages', name='pages_all_pages'),
     url(r'^(?P<slug>[-\w]+)/$', 'pages.views.detail', name='pages_detail_page'),
)