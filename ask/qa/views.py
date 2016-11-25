from django.shortcuts import render
from qa.models import QuestionManager

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def oneQuestion(request,pk):
	ret = "<h1>" + pk + "</h1>"
	return HttpResponse(ret)

def popular(request):
	page = request.GET.get('page')
	return HttpResponse(page)

def index(request):
#	page = request.GET.get('page')
#	return HttpResponse(page)a
	qa=QuestionManager()
	strToRet = qa.new(request.GET.get('page'))
	return HttpResponse(strToRet)
