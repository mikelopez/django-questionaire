from django.db import models


class QuestionaireManager(models.Manager):
    """Questionaire model manager."""
    @classmethod
    def add_question(self, q, **kwargs):
        """Adds a question to a questionaire."""
        if not q:
            return None
        kwargs['parent'] = q
        q = Question(**kwargs)
        q.save()
        return q


class Questionaire(models.Model):
    """
    Questionaire model.
    """
    name = models.CharField(max_length=100)
    objects = QuestionaireManager()
    def questions(self):
        """Returns the QuerySet list of questions."""
        return self.question_set.select_related()

    def add_question(self, **kwargs):
        """Adds a question to a questionaire."""
        q = Questionaire.objects.add_question(self, **kwargs)
        return q


class Question(models.Model):
    """
    Question of a questionaire.
    """
    TYPES = (
        ('text', 'text'),
        ('multiple_choice', 'multiple_choice'),
        ('yes_or_no', 'yes_or_no'),
    )
    question = models.TextField()
    parent = models.ForeignKey('Questionaire')


class Answer(models.Model):
    """
    Answer to a question.
    """
    answer = models.TextField()
    question = models.ForeignKey('Question')
