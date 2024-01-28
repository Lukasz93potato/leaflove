from django.contrib import admin
from .models import Plant, Tag, Description

admin.site.register(Plant)
admin.site.register(Tag)
admin.site.register(Description)