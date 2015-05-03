from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import ArtPiece, Artist, Create, Event, Museum
from django.template import RequestContext, loader, Context, Template
from django.core.urlresolvers import reverse
from django.db import connection

from .forms.VeggieForms import SearchForm, SelectRegionForm, SelectTypeForm, SelectStyleForm

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def search_piece(query):

       # res = ArtPiece.objects.raw("SELECT * FROM art_piece JOIN artist JOIN `create` ON art_piece.art_id = `create`.art_id AND `create`.artist_id=artist.artist_id WHERE art_name LIKE '%%' %s '%%' OR region LIKE '%%' %s '%%' OR style LIKE '%%' %s '%%' OR art_type LIKE '%%' %s '%%' OR description LIKE '%%' %s '%%' OR artist_name LIKE '%%' %s '%%' ", [query, query, query, query, query, query])

       cursor = connection.cursor()
       cursor.execute(
               ''' SELECT *
               FROM art_piece JOIN artist JOIN `create` ON art_piece.art_id = `create`.art_id AND `create`.artist_id=artist.artist_id
               WHERE art_name LIKE '%%' %s '%%'
               OR region LIKE '%%' %s '%%'
               OR style LIKE '%%' %s '%%'
               OR art_type LIKE '%%' %s '%%'
               OR description LIKE '%%' %s '%%'
               OR artist_name LIKE '%%' %s '%%'
               ''', [query, query, query, query, query, query])
       res = dictfetchall(cursor)

       cursor.execute(
               '''SELECT COUNT(*)
               FROM art_piece JOIN artist JOIN `create` ON art_piece.art_id = `create`.art_id AND `create`.artist_id=artist.artist_id
               WHERE art_name LIKE '%%' %s '%%'
               OR artist_name LIKE '%%' %s '%%'
               OR region LIKE '%%' %s '%%'
               OR style LIKE '%%' %s '%%'
               OR art_type LIKE '%%' %s '%%'
               OR description LIKE '%%' %s '%%' ''', [query, query, query, query, query, query])
       row = cursor.fetchone()

       return res, row[0]

# def search_res_num(query):
#         cursor = connection.cursor()
#         cursor.execute('''SELECT COUNT(*) FROM art_piece JOIN artist JOIN `create` ON art_piece.art_id = `create`.art_id AND `create`.artist_id=artist.artist_id WHERE art_name LIKE '%%' %s '%%' OR region LIKE '%%' %s '%%' OR style LIKE '%%' %s '%%' OR art_type LIKE '%%' %s '%%' OR description LIKE '%%' %s '%%' ''', [query, query, query, query, query])
#         row = cursor.fetchone()
#         return row[0]

def search_event(query):
        res = Event.objects.raw("SELECT * FROM event WHERE event_name LIKE '%%' %s '%%'", [query])

        cursor = connection.cursor()
        cursor.execute(
                '''
                SELECT COUNT(*)
                FROM event
                WHERE event_name LIKE '%%' %s '%%'
                ''', [query])

        row = cursor.fetchone()
        return res, row[0]

# def search_collections(region, style, s_type):
# 	query=[]
#         if not region == 'N/A':
#             query.append("region = " + region)

#         if not style == 'N/A':
#             query.append("style = " + style)

#         if not s_type == 'N/A':
#             query.append("s_type = " + s_type)

#         if len(query) == 1:
#             return ArtPiece.objects.raw('select * from art_piece where %s',[query[0]])

# 	elif:
#             queries = query[0]
#             for q in query[1:]:
#                 queries += " AND "
#                 queries += q
#             return ArtPiece.objects.raw('select * from art_piece where %s',[queries])
#         else:
#             return ArtPiece.objects.raw('select * from art_piece')


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        # dropdown queries
        art_region = request.POST.get('region')
        art_type = request.POST.get('type')
        art_style = request.POST.get('style')

        c = RequestContext(request, {
            'r': art_region,
            't': art_type,
            's': art_style,})

        return render(request, 'ms/drop.html', c)

        if form.is_valid():
            # Processing the data, i.e. query them from the database
            search_query = form.cleaned_data['content']

            art_piece_list, piece_num= search_piece(search_query)
            event_list, event_num = search_event(search_query)

            if len(list(art_piece_list)) <= 0:
                art_piece_list = None

            if len(list(event_list)) <= 0:
                event_list = None

            context = RequestContext(request, {
                    'art_piece_list': art_piece_list,
                    'piece_num': piece_num,
                    'event_num': event_num,
                    'event_list': event_list,
                    'query':search_query,
            })

            return render(request, 'ms/results.html',context)

    else:
        form = SearchForm()

    region_list = ["Asian", "African", "North American", "Central & South American", "Ocenanian", "European"]
    type_list = ["Applied & Decorative Arts","Drawing","Painting","Photograph","Print", "Sculpture","Watercolor"]
    style_list = ["Realist","Abstract","Expressionist","Conceptual"]


    return render(request, 'ms/index.html', {'form': form,
                                               'region_list': region_list,
                                               'type_list':type_list,
                                               'style_list':style_list})


def results(request):

    return render(request, 'ms/results_d.html', {})

def thanks(request):
    return render(request, 'ms/thanks.html', {})


# a simple test
# def art_piece(request):
#     art_piece_list = ArtPiece.objects.raw('select * from art_piece order by art_id desc')
# #    template = loader.get_template('ms/art_piece.html')
#     context = RequestContext(request, {
#         'art_piece_list': art_piece_list,
#         })
#     #    return HttpResponse(template.render(context))
#     return render(request, 'ms/art_piece.html', context)
