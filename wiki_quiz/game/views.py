# From django
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.forms import MultipleChoiceField

# from python standard library
from random import choice

# Local
from game.create_questions.create_questions import generate_question, questions
from game.forms import MenuForm


def question(request: HttpRequest) -> HttpResponse:

    # Check if the request made is from 'GET' or 'POST'
    # We only care about POST-requests.
    if request.method == 'POST':
        form = MenuForm(request.POST)

        if form.is_valid():

            # Get data back from form.
            category = form.cleaned_data['category']
            difficulty = form.cleaned_data['difficulty']

            # Fetch all possible question-uris.
            possible_questions = list(questions[category].keys())

            # Generate a question based on those uris.
            question = generate_question(category, choice(possible_questions), 4)
    
            return render(request, 'game/question.html', question.to_dict())

    return render(request, redirect(menu))


def menu(request: HttpRequest) -> HttpResponse:
    data = {'form': MenuForm()}
    
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