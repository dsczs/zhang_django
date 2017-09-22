from django.http import HttpResponse
# Create your views here.


def index(request):     # this is a index view
    return HttpResponse("Hello Python Django")


def t1(request):        # this is a test
    return HttpResponse("Hello Python t1 view")
