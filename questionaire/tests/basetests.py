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