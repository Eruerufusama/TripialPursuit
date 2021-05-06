from django import forms

class MenuForm(forms.Form):
    category = forms.ChoiceField(choices=[
        ('geography', 'geography'),
        ('movie', 'movie'),
    ])
        
    difficulty = forms.ChoiceField(choices=[
        ('easy', 'easy'),
        ('normal', 'normal'),
        ('hard', 'hard')
    ])

    number_of_questions = forms.ChoiceField(choices=[
        (5, 5),
        (10, 10),
        (15, 15),
    ])