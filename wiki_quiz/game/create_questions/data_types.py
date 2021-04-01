
class Answer:
    """
    An object representing an answer, which can be true or false.
    """
    def __init__(self, answer: str, is_correct: bool, message: str):
        self.answer = answer
        self.is_correct = is_correct
        self.message = message


    def to_dict(self) -> dict:
        return {
            "text": self.answer,
            "is_correct": self.is_correct,
            "message": self.message
        }


class Question:
    def __init__(self, question: str="", answers: list=[]):
        self.question = question
        self.answers = answers

    def to_dict(self) -> dict:
        return {
            "question_text": self.question,
            "answers": [answer.to_dict() for answer in self.answers]
        }

    def add_answer(self, answer: Answer) -> None:
        self.answers.append(answer)



