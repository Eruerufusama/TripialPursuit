from os import getcwd
from pprint import pprint
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
        'largest_citys': largest_city_question,
        'land_locked': land_locked_question
    }, 
    'movie': {
        'director': director_question,
        'movie_length': movie_length_question,
        'actors': actors_question,
        'release_year': release_year_question,
        'academy_awards_movie': academy_awards_movie_question,
        'academy_awards_person': academy_awards_person_question,
        'actor_has_actor_parent': actor_has_actor_parent_question
    }
}


def generate_question(question_category: str, question_type: str, n_answers: int, difficulty: str='normal') -> Question:
    """
    Generates a question-object.

    Returns:
        question_category: (str) A category to which the question-type belongs to.
        question_type: (str) A Question-object with n answers, one of which is correct.
    """

    filepath = f'{getcwd()}\\game\\json_data\\{question_type}.json'
    
    # Retrieve n answers from local database.
    data = get_answers(filepath, n_answers, difficulty)

    # Fetch the appropriate function based on question-type.
    question_function = questions[question_category][question_type]

    return question_function(data)


if __name__ == "__main__":
    question = generate_question('movie', 'release_year', 4)
    pprint(question.to_dict())
