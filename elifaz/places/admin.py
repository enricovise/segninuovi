from places.models import *
from hypertext.admin import *

class AddressAdmin(LemmaAdmin):
    pass

class PlaceAdmin(LemmaAdmin):
    pass

site.register(Place, PlaceAdmin)
site.register(Address, AddressAdmin)
