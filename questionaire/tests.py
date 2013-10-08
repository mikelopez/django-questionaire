"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class BaseTest(TestCase):
	"""
	Base Test.
	"""
	def setUp(self):
		pass
	def create_questionaire(self, **kwargs):
		"""
		Creates a Questionaire Object.
		"""
		q = Questionaire(**kwargs)
		q.save()
		return q

	def add_question(self, **kwargs):
		"""
		Add a Question to a Questionaire
		"""
		q = Question(**kwargs)
		q.save()
		return q

	def write_answer(self, **kwargs):
		"""
		Write an answer to a question.
		"""
		a = Answer(**kwargs)
		a.save()
		return a

class SimpleTest(TestCase):
    def setUp(self):
    	pass

    def test_questionaire(self):
    	self.assertTrue(self.create_questionaire("EmployeeSurvey"))

