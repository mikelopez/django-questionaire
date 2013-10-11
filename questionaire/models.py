from django.db import models

# Create your models here.
class Questionaire(models.Model):
	"""
	Questionaire model.
	"""
	name = models.CharField(max_length=100)
    def add_question(self, **kwargs):
        """Adds a question to a questionaire."""
        q = Questionaire.objects.add_question(self, **kwargs)
        return q
	

class Question(models.Model):
	"""
	Question of a questionaire.
	"""
	question = models.TextField()
	parent = models.ForeignKey('Questionaire')


class Answer(models.Model):
	"""
	Answer to a question.
	"""
	answer = models.TextField()
	question = models.ForeignKey('Question')
