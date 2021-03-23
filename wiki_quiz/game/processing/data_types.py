class Question:
    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers

    def to_dict(self):
        return {
            "question_text": self.question,
            "answers": [answer.to_dict() for answer in self.answers]
        }



class Answer:
    def __init__(self, answer: str, is_correct: bool, message: str):
        self.answer = answer
        self.is_correct = is_correct
        self.message = message


    def to_dict(self):
        return {
            "text": self.answer,
            "is_correct": self.is_correct,
            "message": self.message
        }

