from django.shortcuts import render, render_to_response
from django.http      import HttpResponse
from django.template  import RequestContext

def index(request):
  context = RequestContext(request)

  context_dict = {
    'boldmessage': "i'm in fact strong",
  }

  return render_to_response('rango/index.html', context_dict, context)


def about(request):
  return HttpResponse("yes, about that hmm")