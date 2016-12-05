from django.http import HttpResponse


def index(request):
    return HttpResponse("Picture Time")

# Create your views here.
