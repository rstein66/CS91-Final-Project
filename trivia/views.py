from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from models import Flashcard
# Create your views here.

def index(request):
	return HttpResponse("Hello World, you are at the trivia index.")

def FCdetail(request, q_id):
	currQ = get_object_or_404(Flashcard, q_id = q_id)
	#return render(request, 'trivia/templates/trivia/FCdetail.html', {'Question:': currQ})
	return HttpResponse("Question: \n%s" % currQ.question_text)

def FCanswer(request, q_id):
	currA = get_object_or_404(Flashcard, q_id = q_id)
	#return render(request, 'trivia/templates/trivia/FCanswer.html', {'Answer:': currA})

	return HttpResponse("Answer: \n%s" % currA.answer_text)