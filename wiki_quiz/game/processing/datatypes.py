class Question:
    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers


class Answer:
    def __init__(self, answer: str, is_correct: bool, message: str):
        self.answer = answer
        self.is_correct = is_correct
        self.message = message