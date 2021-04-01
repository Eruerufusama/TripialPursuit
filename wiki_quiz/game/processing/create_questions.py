from random import sample
from os import getcwd
from json import load
from random import shuffle, choice
from time import sleep

from data_types import Question, Answer










def get_resource_url(query_data: dict, key: str) -> str:
    return query_data[key]['value'].rsplit('/', 1)[-1].replace('_', ' ')




def get_answers(filepath: str, n_answers: int):
    with open(filepath) as json_file:
        return sample(load(json_file), n_answers)



def capital_question(data):
    answers = []
    for i, element in enumerate(data):
        country = get_resource_url(element, 'country')
        capital = get_resource_url(element, 'capital')

        if i == 0:
            question_text = f'What is the capital of {country}?'
            answers.append(Answer(capital, True, f'That is correct, the capitol of {country} is {capital}'))
        else:
            answers.append(Answer(capital, False, f'That is incorrect, the capitol of {country} is {capital}'))

    shuffle(answers)
    return Question(question_text, answers)

W
def population_question(data) -> Question:
    question_choice = choice(['largest', 'smallest'])
    question_text = f'Which of these countries has the {question_choice} population?'

    answers = []
    for element in data:
        country = get_resource_url(element, 'country')
        population = int(get_resource_url(element, 'population'))
        
        answers.append({'population': population, 'country': country})
    answers.sort(key=lambda x: x['population'], reverse=True if question_choice == 'smallest' else False)

    answers = [
        Answer(
            answer['country'],
            True if i == 0 else False,
            f"That is correct! The population of {answer['country']} is around {round(answer['population'] / 1_000_000, 1)} Million."
            ) for i, answer in enumerate(answers)]
    shuffle(answers)
    return Question(question_text, answers)

        
question = {
    'capital': capital_question,
    'population': population_question,
}


def generate_question(question_type: str, n_answers: int) -> Question:
    data = get_answers(f'{getcwd()}/game/json_data/{question_type}.json', n_answers)
    return question[question_type](data, n_answers)