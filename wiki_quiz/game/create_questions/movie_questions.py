from random import shuffle, choice
from pprint import pprint
from random import sample
try:
    from game.create_questions.data_types import Question, Answer
    from game.create_questions.functions import get_resource_url
except:
    from data_types import Question, Answer
    from functions import get_resource_url


def director_question(data: list) -> Question:
    answers = []
    for i, element in enumerate(data):
        director = get_resource_url(element, "directorLabel")
        movie = get_resource_url(element, "movieLabel")

        if i == 0:
            question_text = f"Who directed {movie}?"
            answers.append(Answer(director, True, f"That is correct, the director of {movie} was {director}."))
        
        else:
            answers.append(Answer(director, False, f"That is incorrect, the director of {movie} was {director}."))
        
    shuffle(answers)
    return Question(question_text, answers)


def movie_length_question(data: list) -> Question:
    question_choice = choice(["longest", "shortest"])
    question_text = f"Which of these movies has the {question_choice} runtime?"

    answers = []
    for element in data:
        movie = get_resource_url(element, "movieLabel")
        runtime = int(get_resource_url(element, "length"))

        answers.append({"movie": movie, "runtime": runtime})
    
    answers.sort(key=lambda x: x['runtime'], reverse=False if question_choice == 'shortest' else True)

    answers = [
        Answer(answer['movie'], True if i == 0 else False, f"That is correct! The runtime of {answer['movie']} is around {answer['runtime'] / 60, 2} Hours.")
        for i, answer in enumerate(answers)
    ]

    shuffle(answers)
    return Question(question_text, answers)


def academy_awards_movie_question(data: list) -> Question:
    answers = []
    for i, element in enumerate(data):
        award_count = get_resource_url(element, "count")
        movie = get_resource_url(element, "movieLabel")

        if i == 0:
            question_text = f"How many academy awards have the movie {movie} wone?"
            answers.append(Answer(award_count, True, f"That is correct, the movie {movie} has wone {award_count} academy awards."))
        
        else:
            answers.append(Answer(award_count, False, f"That is incorrect, the movie {movie} has wone {award_count} academy awards."))
        
    shuffle(answers)
    return Question(question_text, answers)



def academy_awards_person_question(data: list) -> Question:
    answers = []
    for i, element in enumerate(data):
        award_count = get_resource_url(element, "count")
        person = get_resource_url(element, "actorLabel")

        if i == 0:
            question_text = f"How many academy awards have {person} wone?"
            answers.append(Answer(award_count, True, f"That is correct, {person} has wone {award_count} academy awards."))
        
        else:
            answers.append(Answer(award_count, False, f"That is incorrect, {person} has wone {award_count} academy awards."))
        
    shuffle(answers)
    return Question(question_text, answers)


def actors_question(data: list) -> Question:
    question_data = []
    for element in data:
        actors = get_resource_url(element, "actors").split(",")
        movie = get_resource_url(element, "movieLabel")
        question_data.append([movie, set(actors)])

    # Remove actors from other movies to make sure we dont get multiple correct alternatives
    # Removes all actors which were present in both the first movie (we base our question on) and in each other movie
    for i in range(len(question_data) - 1):
        question_data[0][1] - question_data[i+1][1]
    
    # Converts back to list
    for i in range(len(question_data)):
        question_data[i][1] = list(question_data[i][1])
    
    answers = []
    for i, element in enumerate(question_data):
        movie = element[0]
        actor = element[1]
        
        if i == 0:
            two_random_actors = sample(actor, 2)
            question_text = f"In which movie did {two_random_actors[0]} and {two_random_actors[1]} play together?"
            answers.append(Answer(movie, True, f"That is correct, {two_random_actors[0]} and {two_random_actors[1]} played together in {movie}"))
        
        else:
            answers.append(Answer(movie, False, f"That is incorrent, {two_random_actors[0]} and {two_random_actors[1]} played together in {movie}"))
    
    shuffle(answers)
    return Question(question_text, answers)


def release_year_question(data: list) -> Question:
    answers = []
    for i, element in enumerate(data):
        year = get_resource_url(element, "year")
        movie = get_resource_url(element, "movieLabel")

        if i == 0:
            question_text = f"When was the movie {movie} released?"
            answers.append(Answer(year, True, f"That is correct, the movie {movie} was realeased in {year}"))
        
        else:
            answers.append(Answer(year, False, f"That is incorrect, the movie {movie} was realeased in {year}"))
        
    shuffle(answers)
    return Question(question_text, answers)


def actor_has_actor_parent_question(data: list) -> Question:
    answers = []
    for i, element in enumerate(data):
        actor = get_resource_url(element, "actorLabel")
        parent_value = get_resource_url(element, "bool")

        if i == 0:
            question_text = f"Did the actor {actor} have a parent who was also an actor?"
            answer_text = f"That is correct"
            answers.append(Answer(parent_value, True, answer_text))
        
        else:
            answer_text = f"That is incorrect"
            answers.append(Answer(parent_value, False, answer_text))
        
    shuffle(answers)
    return Question(question_text, answers)