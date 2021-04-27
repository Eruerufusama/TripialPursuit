from django import forms

class MenuForm(forms.Form):
    category = forms.ChoiceField(choices=[
        ('geography', 'geography'),
        ('movies', 'movies'),
        ('lucky', "I'm feelin' lucky.")
        ])
        
    difficulty = forms.ChoiceField(choices=[
        ('easy', 'easy',),
        ('normal', 'normal'),
        ('hard', 'hard')
    ])