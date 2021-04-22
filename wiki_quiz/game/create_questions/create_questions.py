from os import getcwd
try:
    from game.create_questions.functions import get_answers
    from game.create_questions.geography_questions import *
    from game.create_questions.movie_questions import *
    from game.create_questions.data_types import Question
except:
    from functions import get_answers
    from geography_questions import *
    from movie_questions import *
    from data_types import Question
   

questions = {
    'geography': {
        'capital': capital_question,
        'population': population_question,
        'island': island_question,
        'currency': currency_question,
        'olympics': olympics_question,
        'country_neighbours': country_neighbors_question,
        'largest_citys': largest_city_question 
    }, 
    'movie': {
        'director': director_question,
        'movie_length': movie_length_question
    }
}


def generate_question(question_category: str, question_type: str, n_answers: int) -> Question:
    """
    Generates a question-object.

    Returns:
        question_category: (str) A category to which the question-type belongs to.
        question_type: (str) A Question-object with n answers, one of which is correct.
    """

    
    # Retrieve n answers from local database.
    data = get_answers(f'{getcwd()}\\game\\json_data\\{question_type}.json', n_answers)

    # Fetch the appropriate function based on question-type.
    question_function = questions[question_category][question_type]

    return question_function(data)


if __name__ == "__main__":
    question = generate_question('geography', 'currency', 4)
    print(question.to_dict)
