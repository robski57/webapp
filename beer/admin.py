from django.contrib import admin
from beer.models import Beer, Brewery

class BeerAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}
        list_display = ('name', 'brewery', 'locality')
        search_fields = ['name']

class BreweryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}
        list_display = ('name', 'brewery', 'locality')
    
    
admin.site.register(Beer, BeerAdmin)
admin.site.register(Brewery)

# Register your models here.
