from django.contrib import admin

from .models import School,Contact
from .models import City
from .models import Partner
from .models import Service
from .models import Chauffer
from .models import Puc
# Register your models here.

admin.site.register(School)
admin.site.register(City)
admin.site.register(Partner)
admin.site.register(Service)
admin.site.register(Chauffer)
admin.site.register(Puc)
admin.site.register(Contact)