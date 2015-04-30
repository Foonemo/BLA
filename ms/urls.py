from django.conf.urls import url
from . import views

urlpatterns = [
     # ex: /ms/
    url(r'^$', views.index, name='index'),
     # ex: /ms/art_piece/
#    url(r'^art_piece/$', views.art_piece),
     # ex: /ms/results/
    url(r'^results/$', views.results, name='results'),
     # ex: /ms/thanks/
    url(r'^thanks/$', views.thanks, name='thanks'),

]
