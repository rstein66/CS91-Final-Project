import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()
from trivia.models import Flashcard, MCQuestion, Choice

def searchDB():
    cardGenerator = Flashcard.objects.all()

    # SAMPLE TAG SEARCH    
    userTags = ['algorithms']

    allTags = []
    cardTags = {}
    for card in cardGenerator:
        tags = card.tags
        tagL = tags.split(",")
        for tag in tagL:

            # create a list of all unique tags in the DB
            if str(tag) not in allTags:
                allTags.append(str(tag))

            # create a dictionary of question:tags for all Q's in DB
            if str(card.question_text) not in cardTags.keys():
                cardTags[str(card.question_text)] = []
            cardTags[str(card.question_text)].append(str(tag))

    filteredQ = []
    for card in cardTags.keys():
        for tag in userTags:
            if tag in cardTags[card]:
                if str(card) not in filteredQ:
                    filteredQ.append(str(card))

    return filteredQ

def genTags():
    cardGenerator = Flashcard.objects.all()

    allTags = []

    for card in cardGenerator:
        tags = card.tags
        tagL = tags.split(",")
        for tag in tagL:

            # create a list of all unique tags in the DB
            if str(tag) not in allTags:
                allTags.append(str(tag))
                
    return allTags

