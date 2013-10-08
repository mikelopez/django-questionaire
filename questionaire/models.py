from django.db import models

# Create your models here.
class Questionaire(models.Model):
	"""
	Questionaire model.
	"""
	name = models.CharField(max_length=100)
	

class Question(models.Model):
	"""
	Question of a questionaire.
	"""
	question = models.Textield()
	parent = models.ForeignKey('Questionaire')


class Answer(models.Model):
	"""
	Answer to a question.
	"""
	answer = models.TextField()
	question = models.ForeignKey('Question')