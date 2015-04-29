from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import ArtPiece, Artist, Create, Event, Museum
from django.template import RequestContext, loader, Context, Template
from django.core.urlresolvers import reverse

from .forms.VeggieForms import SearchForm

def search_one(query):
    if query.lower().find('event'):
        return Event.objects.raw('select * from event')

    elif query.lower().find('exhibition'):
        return Event.objects.raw('select * from event where event_type="Exhibition"')

    else:
        return None


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Processing the data, i.e. query them from the database
            search_query = form.cleaned_data['content']
            # make a query

            result_list = search_one(search_query)

#            result_list = Artist.objects.raw("select * from artist")

            c = RequestContext(request, {'art_piece_list': result_list,
                               'query': search_query})

            return render(request, 'ms/results.html',c)

            # return render(request, 'ms/results.html',
            #               {'result_list': result_list,
            #                'query': search_query})

        else:
            # Direct to an error page
            return HttpResponseRedirect('thanks/')
    else:
        form = SearchForm()


    return render(request, 'ms/index.html', {'form': form})


def results(request):
    return render(request, 'ms/results.html', {})

def thanks(request):
    return render(request, 'ms/thanks.html', {})


# a simple test
def art_piece(request):
    art_piece_list = ArtPiece.objects.raw('select * from art_piece order by art_id desc')
#    template = loader.get_template('ms/art_piece.html')
    context = RequestContext(request, {
        'art_piece_list': art_piece_list,
        })
    #    return HttpResponse(template.render(context))
    return render(request, 'ms/art_piece.html', context)
