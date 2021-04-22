# From django
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.forms import MultipleChoiceField

# from python standard library
from random import choice

# Local
from game.create_questions.create_questions import generate_question, questions
from game.forms import MenuForm


def question(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form = MenuForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data['category']

            possible_questions = list(questions[category].keys())
            question = generate_question(category, choice(possible_questions), 4)
    
            return render(request, 'game/question.html', question.to_dict())


def menu(request: HttpRequest) -> HttpResponse:
    form = MenuForm()
    data = {
        'categories': ['geography', 'movies', "im feelin' lucky"],
        'form': form
    }
    
    return render(request, 'game/menu.html', data)
    


def about(request: HttpRequest) -> HttpResponse:
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