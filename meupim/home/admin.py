from django.contrib import admin

from .models import Uf
from .models import Cidade

admin.site.register(Uf)
admin.site.register(Cidade)

