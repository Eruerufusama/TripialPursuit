from django import forms

class MenuForm(forms.Form):
    category = forms.ChoiceField(choices=[
        ('geography', 'geography'),
        ('movies', 'movies'),
        ('lucky', "I'm feelin' lucky.")
        ])
    difficulty = forms.ChoiceField(choices=[
        ('1', 'easy',),
        ('2', 'intermediate'),
        ('3', 'hard')
    ])