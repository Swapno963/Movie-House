from django.contrib import admin

# Register your models here.
from . import models

class MovieModelAdmin(admin.ModelAdmin):
    list_display = ['title','category','description','rating','price']
admin.site.register(models.MoviesModel,MovieModelAdmin)