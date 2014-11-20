from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from models import Flashcard
# Create your views here.

def index(request):
	latest_question_list = Flashcard.objects.all()
	template = loader.get_template('trivia/index.html')
	context = RequestContext(request, {'latest_question_list':latest_question_list})
	return HttpResponse(template.render(context))

def FCques(request, q_id):
	question = Flashcard.objects.get(q_id = q_id)
	template = loader.get_template('trivia/FCques.html')
	context = RequestContext(request, {'question':question})
	return HttpResponse(template.render(context))

def FCanswer(request, q_id):
	question = Flashcard.objects.get(q_id = q_id)
	# currA = get_object_or_404(Flashcard, q_id = q_id)
	# return render(request, 'trivia/templates/trivia/FCanswer.html', {'Answer:': currA})
	template = loader.get_template('trivia/FCans.html')
	context = RequestContext(request, {'question':question})
	return HttpResponse(template.render(context))