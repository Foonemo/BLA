from django.shortcuts import render
from django.http import HttpResponse
from .models import ArtPiece
from django.template import RequestContext, loader, Context, Template
from .forms.VeggieForms import SearchForm


def get_searchContent(request):
    if request.method == 'GET':
        form = SearchForm()
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            return HttpResponseReidrect('/thanks/')

    return render(request, 'ms/index.html', {'form': form,})

def index(request):
    return get_searchContent(request)


def result(request):
    context = Context()
    return render(request, 'ms/results.html', context)



# a simple test
def art_piece(request):
    art_piece_list = ArtPiece.objects.raw('select * from art_piece order by art_id desc')
#    template = loader.get_template('ms/art_piece.html')
    context = RequestContext(request, {
        'art_piece_list': art_piece_list,
        })
    #    return HttpResponse(template.render(context))
    return render(request, 'ms/art_piece.html', context)
