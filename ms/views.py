from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from ms.models import ArtPiece

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Museum Search System - BLA Power By Veggie Birds.")

# def result(request, query_id):
#     response = "query number: "
#     return HttpResponse(response % query_id)

class ListArtPieceView(ListView):
    model = ArtPiece
