from django.shortcuts import render
from django.http import HttpResponse
from .models import ArtPiece
from django.template import RequestContext, loader, Context, Template


# Create your views here.
def index(request):
#    template = loader.get_template('ms/index.html')
    context = Context()
    return render(request, 'ms/index.html', context)


def art_piece(request):
    art_piece_list = ArtPiece.objects.raw('select * from art_piece order by art_id desc')
#    template = loader.get_template('ms/art_piece.html')
    context = RequestContext(request, {
        'art_piece_list': art_piece_list,
        })
    #    return HttpResponse(template.render(context))
    return render(request, 'ms/art_piece.html', context)
