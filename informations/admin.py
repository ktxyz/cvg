from django.contrib import admin

from .models import InformationMeta
from .models import InformationDetail

admin.site.register(InformationMeta)
admin.site.register(InformationDetail)