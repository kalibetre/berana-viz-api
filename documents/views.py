from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def get_document(request) -> str:
    return HttpResponse("My Document")
