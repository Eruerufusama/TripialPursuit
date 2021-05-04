# From django
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.forms import MultipleChoiceField

# from python standard library
from random import choice

# From local
from game.create_questions.main import generate_question, QUESTIONS, BINARY_QUESTIONS
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
            number_of_questions = int(form.cleaned_data['number_of_questions'])

            # Fetch all possible question-uris.
            possible_questions = list(QUESTIONS[category].keys())

            # Generate questions based on those uris.
            _questions = []
            for _ in range(number_of_questions):
                question_key = choice(possible_questions)
                _questions.append(generate_question(category, question_key, 2 if question_key in BINARY_QUESTIONS else 4).to_dict())

            # Render website.
            return render(request, 'game/question.html', {"questions": _questions})
    

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