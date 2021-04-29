from django import forms

class MenuForm(forms.Form):
    category = forms.ChoiceField(choices=[
        ('geography', 'geography'),
        ('movies', 'movies'),
        ('lucky', "I'm feelin' lucky.")
    ])
        
    difficulty = forms.ChoiceField(choices=[
        ('easy', 'easy'),
        ('normal', 'normal'),
        ('hard', 'hard')
    ])

    n_questions = forms.ChoiceField(choices=[
        (5, '5'),
        (10, '10'),
        (20, '20'),
        (50, '50'),
    ])