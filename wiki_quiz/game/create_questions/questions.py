from random import shuffle, choice
from game.create_questions.data_types import Question, Answer
from game.create_questions.functions import get_resource_url


def capital_question(data: list) -> Question:

    # Create answers.
    answers = []
    for i, element in enumerate(data):

        # Create useful data from urls.
        country = get_resource_url(element, 'country')
        capital = get_resource_url(element, 'capital')

        # First element is the correct answer.
        if i == 0:
            question_text = f'What is the capital of {country}?'
            answers.append(Answer(capital, True, f'That is correct, the capitol of {country} is {capital}'))
        else:
            answers.append(Answer(capital, False, f'That is incorrect, the capitol of {country} is {capital}'))


    shuffle(answers)
    return Question(question_text, answers)


def population_question(data: list) -> Question:
    question_choice = choice(['largest', 'smallest'])
    question_text = f'Which of these countries has the {question_choice} population?'

    # Create answers.
    answers = []
    for element in data:

        # Create useful data from urls.
        country = get_resource_url(element, 'country')
        population = int(get_resource_url(element, 'population'))

        # Format so it's easy to work with.
        answers.append({'population': population, 'country': country})

    # Sort from largest population to smallest, or reverse.
    answers.sort(key=lambda x: x['population'], reverse=False if question_choice == 'smallest' else True)

    # Creates answer-objects.
    answers = [
        Answer(answer['country'], True if i == 0 else False, f"That is correct! The population of {answer['country']} is around {round(answer['population'] / 1_000_000, 1)} Million.")
        for i, answer in enumerate(answers)
        ]


    shuffle(answers)
    return Question(question_text, answers)