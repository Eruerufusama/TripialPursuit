from django.shortcuts import render

# Erstatt denne commenten med en import til python-filen som genererer spørsmål.
from game.processing.reworked import CountryQuestionGenerator, QuestionGenerator


def question(request):
    """
    Creates a general website for questions.
    """

    question_generator = QuestionGenerator()
    question_generator.query_to_json()
    
    country_question_generator = CountryQuestionGenerator()
    question = country_question_generator.get_population_question()

    return render(request, 'game/question.html', question.to_dict())


def menu(request):
    return render(request, 'game/menu.html')


















# question = {
#     'question_text': 'Which of these cities is furthest south?',
#     'answers': [
#         {
#             'text': 'Johannesburg',
#             'is_correct': False,
#             'message': "noe her"
#         },
#                 {
#             'text': 'Sydney',
#             'is_correct': False,
#             'message': "noe her"
#         },
#                 {
#             'text': 'Buenos Aires',
#             'is_correct': True,
#             'message': "noe her"
#         },
#                 {
#             'text': 'Santiago',
#             'is_correct': False,
#             'message': "noe her"
#         }
#     ]
# }