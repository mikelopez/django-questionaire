"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from basetests import *

class QuestionaireTestCase(BaseTest):
    """
    Questionaire Test Case.
     - Create a Questionaire
     - Create questions on the Questionaire 
     - Create answers to questions.
     - Get answers to questions (by user, or all)
     - Check if the user has completed all answers to a specific questionaire.
    """

    def setUp(self):
        pass

    def test_questionaire(self):
        """Creates a new Questionaire."""
        self.assertTrue(self.create_questionaire(name="EmployeeSurvey"))

    def test_add_question(self):
        """Creates some questions on the questionaire."""
        self.assertTrue(self.add_question(question="Do you like the color blue?"))

    def test_add_answer(self):
        """Creates an answer for the questions on a questionaire."""
        question = self.add_question(question="Do you like fishsticks?",
                                     parent=self.create_questionaire(name="UserSurvey"))
        self.assertTrue(write_answer(answer="Sometimes, I do", 
                                     question=question))

