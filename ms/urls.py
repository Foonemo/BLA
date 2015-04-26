from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     # ex: /ms/5/art_piece
    url(r'art_piece/', views.art_piece),#, name='art_piece'),
]
