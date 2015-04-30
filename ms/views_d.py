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
		cursor = connection.cursor()
		cursor.execute("SELECT * from art_piece JOIN create JOIN artist WHERE
			style = abstract)
		#cursor.execute("SELECT * from art_piece JOIN create JOIN artist WHERE
		#	name LIKE %s OR region LIKE %s OR style LIKE %s OR type LIKE %s
		#	OR description LIKE %s", [query])
		return cursor.fetchall()
        #return None
		
def search_collections(region,style,type):
	query=[]
	if region and region.strip()
		query.append("region = " + region);
	if style and style.strip()
		query.append("style = " + style);
	if type and type.strip()
		query.append("type = " + type);
		
	if len(query) = 1
		return ArtPiece.objects.raw('select * from art_piece where %s',[query[0]])
		#return return ArtPiece.objects.raw('select * from art_piece where %s',(query[0])
	else
		queries = query[0]
		for x in range(1, len(query)):
			queries += "AND" 
			queries += query[x]
		return ArtPiece.objects.raw('select * from art_piece where %s',[queries])

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
		region_form = SelectRegionForm(request.POST)
        if form.is_valid():
            # Processing the data, i.e. query them from the database
            search_query = form.cleaned_data['content']
			
			region = region_form.cleaned_data['region_choice']
			#region = request.POST.get['region_choice'] 
			style = region_form.cleaned_data['style_choice']
			type = region_form.cleaned_data['type_choice']
			
            # make a query
			
            if search_query and search_query.strip() 
				result_list = search_one(search_query)
			else region or style or type	
				result_list = search_collections(region,style,type)

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