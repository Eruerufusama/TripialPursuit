from random import choice
from django.shortcuts import render
from game.create_questions.create_questions import generate_question

# Gammel kode.
# from game.create_questions.reworked import CountryQuestionGenerator, QuestionGenerator

# def question(request) -> 'HttpResponse':
#     """
#     Creates a general website for questions.
#     """

#     question_generator = QuestionGenerator()
#     question_generator.query_to_json()
    
#     country_question_generator = CountryQuestionGenerator()
#     question = country_question_generator.get_population_question()

#     return render(request, 'game/question.html', question.to_dict())


def question(request) -> 'HttpResponse':

    possible_questions = ['capital', 'population']

    question = generate_question(choice(possible_questions), 4)
    return render(request, 'game/question.html', question.to_dict())




def menu(request):
    data = {
        'categories': ['geography', 'sports', 'movies', "im feelin' lucky"]
    }

    return render(request, 'game/menu.html', data)



def about(request):
    return render(request, 'game/about.html')


















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