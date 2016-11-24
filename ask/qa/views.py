from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def oneQuestion(request,pk):
	ret = "<h1>" + pk + "</h1>"
	return HttpResponse(ret)

def popular(request,page_num):
	ret = page_num
	return HttpResponse(ret)

def index(request,page_num):
	return HttpResponse(page_num)
