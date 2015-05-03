from django.conf.urls import url
from . import views

urlpatterns = [
     # ex: /ms/
    url(r'^$', views.index, name='index'),
     # ex: /ms/results/
    url(r'^results/$', views.results, name='results'),

    # ex: /ms/results/events
    url(r'^results/events/$', views.results_events, name='events'),
    # ex: /ms/results/art_piece
    url(r'^results/art_pieces/$', views.results_artpieces, name='art_pieces'),

     # ex: /ms/thanks/
    url(r'^thanks/$', views.thanks, name='thanks'),



]
