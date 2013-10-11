from django.db import models

class QuestionaireManage(models.Manager):
    """Questionaire model manager."""
    @classmethod
    def add_question(self, q, **kwargs):
        """Adds a question to a questionaire."""
        if not q:
            return None
        kwargs['questionaire'] = q
        q = Question(**kwargs)
        q.save()
        return q

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
