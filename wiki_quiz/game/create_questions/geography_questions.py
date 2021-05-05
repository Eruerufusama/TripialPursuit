from random import shuffle, choice
try:
    from game.create_questions.data_types import Question, Answer
    from game.create_questions.functions import get_resource_url
except:
    from data_types import Question, Answer
    from functions import get_resource_url


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
            question_text = f'What country is the island {island} located in?'
            answer_text = f'That is correct, the island {island} is located in {country}.'
            answers.append(Answer(country, True, answer_text))

        else:
            answer_text = f'That is incorrect, the island {island} is located in {country}.'
            answers.append(Answer(country, False, answer_text))

    shuffle(answers)
    return Question(question_text, answers)


def currency_question(data: list) -> Question:
    answers = []

    for i, element in enumerate(data):
        country = get_resource_url(element, "country")
        currency_code = element["currencyCode"]["value"]
        
        if i == 0:
            question_text = f"What currency code does {country} use?"
            answer_text = f"That is correct {country} has {currency_code} as their currency code."
            answers.append(Answer(currency_code, True, answer_text))
        
        else:
            answer_text = f"That is incorrect, {country} has {currency_code} as their currency code."
            answers.append(Answer(currency_code, False, answer_text))
    
    shuffle(answers)
    return Question(question_text, answers)


def olympics_question(data: list) -> Question:
    
    answers = []
    for i, element in enumerate(data):

        country = get_resource_url(element, 'country')
        olympic = get_resource_url(element, 'olympic')

        if i == 0:
            question_text = f'What country hosted the {olympic} olympics?'
            answer_text = f'That is correct, {country} hosted the {olympic} olympics.'
            answers.append(Answer(country, True, answer_text))

        else:
            answer_text = f'That is incorrect, {country} hosted the {olympic} olympics.'
            answers.append(Answer(country, False, answer_text))

    shuffle(answers)
    return Question(question_text, answers)


def country_neighbors_question(data: list) -> Question:
    
    answers = []
    for i, element in enumerate(data):
        
        start_country = get_resource_url(element, "startLabel")
        middle_country = get_resource_url(element, "middleLabel")
        end_country = get_resource_url(element, "endLabel")

        if i == 0:
            question_text = f"What country connects {start_country} and {end_country}?"
            answers_text = f"That is correct, {middle_country} connects {start_country} and {end_country}."
            answers.append(Answer(middle_country, True, answers_text))

        else:
            answer_text = f"That is incorrect, {middle_country} connects {start_country} and {end_country}."
            answers.append(Answer(middle_country, False, answer_text))
    
    shuffle(answers)
    return Question(question_text, answers)


def largest_city_question(data: list) -> Question:
    question_choice = choice(['largest', 'smallest'])  
    question_text = f'Which of these citys has the {question_choice} population?' 

    answers = []
    for element in data:  
        city = get_resource_url(element, "cityLabel")
        population = int(get_resource_url(element, 'population'))
        
        answers.append({'population': population, 'city': city})

    answers.sort(key=lambda x: x['population'], reverse=False if question_choice == 'smallest' else True)

    answers = [
        Answer(answer['city'], True if i == 0 else False, f"That is correct! The population of {answer['city']} is around {round(answer['population'] / 1_000_000, 1)} Million.")
        for i, answer in enumerate(answers)
    ]


    shuffle(answers)
    return Question(question_text, answers)


def land_locked_question(data: list) -> Question:
    answers = []

    for i, element in enumerate(data):
        
        country = get_resource_url(element, "countryLabel")
        locked_value = get_resource_url(element, "locked")

        if i == 0:
            question_text = f'Is {country} landlocked?'
            answer_text = f'That is correct'
            answers.append(Answer(locked_value, True, answer_text))

        else:
            answer_text = f'That is incorrect'
            answers.append(Answer(locked_value, False, answer_text))

    shuffle(answers)
    return Question(question_text, answers)