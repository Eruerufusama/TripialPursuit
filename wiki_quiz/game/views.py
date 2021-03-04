from django.shortcuts import render



def question(request):
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