from django.shortcuts import render
from django.template import RequestContext
from beer.models import Beer, Brewery

def BeersAll(request):
        beers = Beer.objects.all().order_by('name')
        context = {'beers': beers}
        return render(request,'home.html', context, context_instance=RequestContext(request))

def SpecificBeer(request, beerslug):
        beer = Beer.objects.get(slug=beerslug)
        context = {'beer': beer}
        return render(request,'singlebeer.html', context, context_instance=RequestContext(request))

def SpecificBrewery(request, breweryslug):
        brewery = Brewery.objects.get(slug=breweryslug)
        beers = Beer.objects.filter(brewery=brewery)
        context = {'beers': beers}
        return render(request,'singlebrewery.html', context, context_instance=RequestContext(request))

def base(request):
        if request.method == 'GET':
                return render(request, 'webapp/base.html')

