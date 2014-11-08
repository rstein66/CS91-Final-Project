from django.contrib import admin
from trivia.models import MCQuestion
from trivia.models import Flashcard
from trivia.models import Choice
# Register your models here.

admin.site.register(MCQuestion)
admin.site.register(Choice)
admin.site.register(Flashcard)
