from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import ArtPiece, Artist, Create, Event, Museum
from django.template import RequestContext, loader, Context, Template
from django.core.urlresolvers import reverse
from django.db import connection

from .forms.VeggieForms import SearchForm, SelectRegionForm, SelectTypeForm, SelectStyleForm


def search_piece(query):
        return ArtPiece.objects.raw("SELECT * FROM art_piece JOIN artist JOIN `create` ON art_piece.art_id = `create`.art_id AND `create`.artist_id=artist.artist_id WHERE style=%s ", [query])

def search_event(query):
    if query.lower().find('event') != -1:
        return Event.objects.raw('select * from event')

    elif query.lower().find('exhibition') != -1:
        return Event.objects.raw('select * from event where event_type="Exhibition"')

    return []

# def search_collections(region,style,s_type):
# 	query=[]
#         if not region == 'N/A':
# 		query.append("region = " + region)

#         if not style == 'N/A':
# 		query.append("style = " + style)

#         if not s_type == 'N/A':
# 		query.append("s_type = " + s_type)

#         if len(query) == 1:
# 		return ArtPiece.objects.raw('select * from art_piece where %s',[query[0]])
# 		#return return ArtPiece.objects.raw('select * from art_piece where %s',(query[0])
# 	elif:
# 		queries = query[0]
#                 for q in query[1:]:
#                     queries += " AND "
#                     queries += q
#                 return ArtPiece.objects.raw('select * from art_piece where %s',[queries])
#         else:
#             return ArtPiece.objects.raw('select * from art_piece')


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Processing the data, i.e. query them from the database
            search_query = form.cleaned_data['content']

            # s_region = request.POST.get['region']
            # s_style = request.POST.get['style']
            # s_type = request.POST.get['type']
            # make a query


            art_piece_list = search_piece(search_query)
            if len(list(art_piece_list)) <= 0:
                art_piece_list = None

            event_list = search_event(search_query)
            if len(list(event_list)) <= 0:
                event_list = None


            c = RequestContext(request, {
                'art_piece_list': art_piece_list,
                'event_list': event_list,
                'query':search_query,

            })

            return render(request, 'ms/results.html',c)

        else:
            # Direct to an error page
            return HttpResponseRedirect('thanks/')
    else:
        form = SearchForm()

    region_list = ["N/A","Asian", "African", "North American", "Central & South American", "Ocenanian", "European"]
    type_list = ["N/A","Applied & Decorative Arts","Drawing","Painting","Photograph","Print", "Sculpture","Watercolor"]
    style_list = ["N/A","Realist","Abstract","Expressionist","Conceptual"]


    return render(request, 'ms/index_d.html', {'form': form,
                                               'region_list': region_list,
                                               'type_list':type_list,
                                               'style_list':style_list})


def results(request):
    return render(request, 'ms/results_d.html', {})

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
