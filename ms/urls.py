from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     # ex: /ms/art_piece/
    url(r'art_piece/', views.art_piece),
     # ex: /ms/results/
    url(r'results/', views.result),
]
