from django.contrib import admin
from beer.models import Beer, Brewery

class BeerAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}
        list_display = ('name', 'brewery', 'locality')
        search_fields = ['name']

class BreweryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}

class TinyMCEAdmin(admin.ModelAdmin):
        class Media:
                js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)        

admin.site.register(Beer, BeerAdmin)
admin.site.register(Brewery, BreweryAdmin)
