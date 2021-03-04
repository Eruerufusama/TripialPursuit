from django.shortcuts import render
# Erstatt denne commenten med en import til python-filen som genererer spørsmål.


def question(request):
    # Erstatt denne commenten med en instans av et generert spørsmål.

    # Her er et eksempel-spørsmål som vi kan generere.
    # Vi kan selvsagt legge til mer metadata til denne.
    question = {
    'question_text': 'Which of these cities is furthest south?',
    'answers': [
        {
            'text': 'Johannesburg',
            'is_correct': False,
        },
                {
            'text': 'Sydney',
            'is_correct': False,
        },
                {
            'text': 'Buenos Aires',
            'is_correct': True,
        },
                {
            'text': 'Santiago',
            'is_correct': False,
        }
    ]
}
    return render(request, 'game/question.html', question)