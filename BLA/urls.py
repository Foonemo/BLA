from django.conf.urls import patterns, include, url
from django.contrib import admin

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'BLA.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^ms/', 'ms.views.index'),
#     url(r'^ms/(?P<slug>[-\w]+)/$', 'ms.views.result'),
# ]


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ms.views.index'),
#    url(r'^ms/(?P<slug>[-\w]+)/$', 'ms.views.result'),
)
