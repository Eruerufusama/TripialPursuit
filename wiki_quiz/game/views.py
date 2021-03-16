from django.shortcuts import render

# Erstatt denne commenten med en import til python-filen som genererer spørsmål.
from reworked import CountryQuestionGenerator



def question(request):
    # Erstatt denne commenten med en instans av et generert spørsmål.
    generator = CountryQuestionGenerator()
    question = generator.generate_question("capital")

    return render(request, 'game/question.html', question)


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