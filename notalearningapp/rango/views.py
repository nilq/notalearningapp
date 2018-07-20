from django.shortcuts import render
from django.http      import HttpResponse

def index(request):
  return HttpResponse("yes hello")


def about(request):
  return HttpResponse("yes, about that hmm")