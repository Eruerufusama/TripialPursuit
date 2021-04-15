from os import getcwd
try:
    from game.create_questions.functions import get_answers
    from game.create_questions.questions import *
    from game.create_questions.data_types import Question
except:
    from functions import get_answers
    from geography_questions import *
    from data_types import Question
   

questions = {
    'capital': capital_question,
    'population': population_question,
    'island': island_question,
    'olympics': olympics_question,
    'country_neighbours': country_neighbors_question,
    'largest_citys': largest_city_question 
}


def generate_question(question_type: str, n_answers: int) -> Question:
    """
    Generates a question-object.

    Returns:
        [type]: (Question) A Question-object with n answers, one of which is correct.
    """

    
    # Retrieve n answers from local database.
    data = get_answers(f'{getcwd()}\\game\\json_data\\{question_type}.json', n_answers)

    # Fetch the appropriate function based on question-type.
    question_function = questions[question_type]

    return question_function(data)


if __name__ == "__main__":
    question = generate_question('largest_citys', 4)
    print(question.to_dict)