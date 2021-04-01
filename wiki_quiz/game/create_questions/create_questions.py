from os import getcwd
from game.create_questions.functions import get_answers
from game.create_questions.questions import capital_question, population_question



def main():
    question = generate_question('population', 2)

    print(question.question)
    for answer in question.answers:
        print(answer.answer, answer.is_correct)


   
questions = {
    'capital': capital_question,
    'population': population_question,
}


def generate_question(question_type: str, n_answers: int):
    # Retrieve n answers from local database.
    data = get_answers(f'{getcwd()}/game/json_data/{question_type}.json', n_answers)

    # Fetch the appropriate function based on question-type.
    question_function = questions[question_type]

    return question_function(data)


if __name__ == "__main__":
    main()