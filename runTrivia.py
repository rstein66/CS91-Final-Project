import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
from trivia.models import Flashcard, MCQuestion, Choice

def main():
    cardGenerator = Flashcard.objects.all()
    
    tagSearch = raw_input("Search for question tags, separated by commas: ")
    userTags = tagSearch.split(",")

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

    if len(filteredQ) == 0:
        print "Could not find any questions with those tags."
    else:
        print "Found the following relevant questions:"
        for q in filteredQ:
            print q



    

main()

