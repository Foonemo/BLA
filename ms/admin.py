from django.contrib import admin

# Register your models here.
from .models import ArtPiece, Artist, Create, Event, Museum

admin.site.register(ArtPiece)
admin.site.register(Artist)
admin.site.register(Create)
admin.site.register(Event)
admin.site.register(Museum)
