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



def island_question(data: list) -> Question:

    answers = []
    for i, element in enumerate(data):

        country = get_resource_url(element, 'country')
        island = get_resource_url(element, 'island')

        if i == 0:
            question_text = f"What country is the island {island} located in?"
            answer_text = f"That is correct, the island {island} is located in {country}."
            answers.append(Answer(country, True, answer_text))

        else:
            answer_text = f"That is incorrect, the island {island} is located in {country}."
            answers.append(Answer(island, False, answer_text))

        shuffle(answers)
        return Question(question_text, answers)



def olympics_question(data: list) -> Question:
    
    answers = []
    for i, element in enumerate(data):

        country = get_resource_url(element, "country")
        olympic = get_resource_url(element, "olympic")

        if i == 0:
            question_text = f"What country hosted the {olympic} olymics?"
            answer_text = f"That is correct, {country} hosted the {olympic} olympics."
            answers.append(Answer(country, True, answer_text))

        else:
            answer_text = f"That is incorrect, {country} hosted the {olympic} olympics."
            answers.append(Answer(country, False, answer_text))

    shuffle(answers)
    return Question(question_text, answers)


def 