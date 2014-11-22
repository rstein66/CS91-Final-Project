import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()
from trivia.models import Flashcard, MCQuestion, Choice

# searches DB for all questions tagged with the input category.
# assumes no question has 2 identical tags, so that no question
# is duplicated in the output question list
def searchFlashDB(category):
    cardGenerator = Flashcard.objects.all()

    Qlist = []
    for card in cardGenerator:
        tags = card.tags
        tagL = tags.split(",")
        for tag in tagL:

            # create a list of all unique tags in the DB
            if str(tag) == category:
                Qlist.append(card)

    return Qlist

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