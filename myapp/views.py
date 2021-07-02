from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest,JsonResponse

# Create your views here.
def myfunctioncall(request):
    return HttpResponse('Hello World Django')