from django.db import models

# Create your models here.

# question for flashcard mode
class Flashcard(models.Model):
    question_text = models.CharField(max_length = 350)
    # tags will be concatenated as a comma-delimited string
    tags = models.CharField(max_length = 350, default = 'empty')
    answer_text = models.CharField(max_length = 350)
    q_id = models.IntegerField(default = '0')

    def get(self):
        return self.Flashcard


# question for game mode
class MCQuestion(models.Model):
    question_text = models.CharField(max_length = 350)
    Answer_A = "A"
    Answer_B = "B"
    Answer_C = "C"
    Answer_D = "D"

    A = models.CharField(max_length = 100, default = 'empty')
    B = models.CharField(max_length = 100, default = 'empty')
    C = models.CharField(max_length = 100, default = 'empty')
    D = models.CharField(max_length = 100, default = 'empty')   
    Answer_Choices = ((Answer_A, A),  (Answer_B, B), (Answer_C, C),  (Answer_D, D))

    answers = models.CharField(max_length = 1, choices = Answer_Choices, default = 'E')
    correct = models.CharField(max_length = 1, default = 'E')

    scorePercentage = models.IntegerField(default = 0)

# For game mode only
class Choice(models.Model):
    question = models.ForeignKey(MCQuestion)
    answer = models.CharField(max_length = 10)
