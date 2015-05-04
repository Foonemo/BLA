from django.conf.urls import url
from . import views

urlpatterns = [
     # ex: /ms/
    url(r'^$', views.index, name='index'),
     # ex: /ms/results/
    url(r'^results/$', views.results, name='results'),
    # ex: /ms/results/events
    url(r'^results/search_events_(?P<search_query>[a-zA-Z]+)/$', views.results_events, name='results_events'),
    # ex: /ms/results/art_piece
    url(r'^results/search_artpieces_(?P<search_query>[a-zA-Z]+)/$', views.results_artpieces, name='results_artpieces'),

     # ex: /ms/thanks/
    url(r'^thanks/$', views.thanks, name='thanks'),



]
