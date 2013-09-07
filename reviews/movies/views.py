# Create your views here.

from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

def test(request):
    """


    :return:
    """
    return render_to_response('test.html','',context_instance=RequestContext(request))


def getdata(request):
    data = ['Chennai Express','1000 abadalu','Jobs','Bhaag Milka Bhaag','Athariintiki Dariedi']
    return HttpResponse(json.dumps({'data':data}))