from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from models import Flashcard, MCQuestion
from searchDB import searchDB, genTags
import random
# Create your views here.

# home page
def home(request):
	template = loader.get_template('trivia/home.html')
	context = RequestContext(request, {'fake':'dictionary'})
	return HttpResponse(template.render(context))

def FCanswer(request, category, q_id):
	question = Flashcard.objects.get(q_id = q_id)
	next_id = question.q_id + 1
	template = loader.get_template('trivia/FCans.html')
	context = RequestContext(request, {'question':question, 'id':next_id})
	return HttpResponse(template.render(context))

# page to select tags to search by
def chooseTag(request):
	tagList = genTags('flashcard')
	template = loader.get_template('trivia/tags.html')
	context = RequestContext(request, {'tags':tagList})
	return HttpResponse(template.render(context))

# page to select game mode
def mode(request):
	template = loader.get_template('trivia/mode.html')
	context = RequestContext(request, {'fake':'dictionary'})
	return HttpResponse(template.render(context))

# about page
def about(request):
	template = loader.get_template('trivia/about.html')
	context = RequestContext(request, {'fake':'dictionary'})
	return HttpResponse(template.render(context))

# WHAT TO DO IF NO QUESTIONS ARE AVAILABLE FOR THE TAG????
def randomFC(request, category):
	Qlist = searchDB(category, 'flashcard')
	randomQ = random.choice(Qlist)
	template = loader.get_template('trivia/FCques.html')
	context = RequestContext(request, {'question':randomQ, 'id':randomQ.q_id, 'category':category})
	return HttpResponse(template.render(context))

def returnFC(request, category, q_id):
	question = Flashcard.objects.get(q_id = q_id)
	template = loader.get_template('trivia/return.html')
	context = RequestContext(request, {'question':question})
	return HttpResponse(template.render(context))

def chooseTagMC(request):
	tagList = genTags('multiple choice')
	template = loader.get_template('trivia/MCtags.html')
	context = RequestContext(request, {'tags':tagList})
	return HttpResponse(template.render(context))

def randomMC(request, category):
	Qlist = searchDB(category, 'multiple choice')
	randomQ = random.choice(Qlist)
	template = loader.get_template('trivia/MCques.html')
	context = RequestContext(request, {'question':randomQ, 'id':randomQ.q_id, 'category':category})
	return HttpResponse(template.render(context))

def checkAns(request, category, q_id, answer):
	question = MCQuestion.objects.get(q_id = q_id)
	if answer != question.correct:
		template = loader.get_template('trivia/wrong.html')
		question.numWrong = question.numWrong + 1
		question.save()
	else:
		template = loader.get_template('trivia/right.html')
		question.numCorrect = question.numCorrect + 1
		question.save()

	context = RequestContext(request, {'question':question, 'category':category, 'usrAnswer':answer, 'id':question.q_id})
	return HttpResponse(template.render(context))