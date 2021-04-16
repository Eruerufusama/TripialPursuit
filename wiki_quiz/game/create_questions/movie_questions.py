from random import shuffle, choice
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
