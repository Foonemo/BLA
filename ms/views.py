from django.shortcuts import render
from django.http import HttpResponse
from .models import ArtPiece
from django.template import RequestContext, loader


# Create your views here.
def index(request):
    return HttpResponse("Welcome to Museum Search System - BLA \n Power By Veggie Birds.")


def art_piece(request):
    art_piece_list = ArtPiece.objects.raw('select * from art_piece order by art_id desc')
    template = loader.get_template('ms/art_piece.html')
    context = RequestContext(request, {
        'art_piece_list': art_piece_list,
        })
    return HttpResponse(template.render(context))
