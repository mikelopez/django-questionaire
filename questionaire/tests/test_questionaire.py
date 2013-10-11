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

    def test_question_types(self):
        """Checks for the right question types."""
        types = Question.TYPES
        for val in ['yes_or_no', 'multiple_choice', 'text']:
            self.assertTrue([t for t in types if val in ])


    def test_questionaire(self):
        """Creates a new Questionaire."""
        self.assertTrue(self.create_questionaire(name="EmployeeSurvey"))

    def test_add_question(self):
        """Creates some questions on the questionaire."""
        questionaire = self.create_questionaire(name="ABC")
        question = questionaire.add_question(question="Do you like the color blue?", 
                                             parent=questionaire)
        self.assertEquals(questionaire.questions.count(), 1)

    def test_add_answer(self):
        """Creates an answer for the questions on a questionaire."""
        questionaire = self.create_questionaire(name="UserSurvey")
        questionaire.save()
        question = questionaire.add_question(question="Do you like fishsticks?", 
                                     parent=questionaire)
        question.save()
        self.assertTrue(self.write_answer(answer="Sometimes, I do", 
                                         question=question))


    #def test_question_types(self):
        #"""Creates questionaire and tests come functionality."""
        #q = self.create_questionaire
