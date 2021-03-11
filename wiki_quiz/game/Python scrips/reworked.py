from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
from random import shuffle, choice

class Question:
    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers


class Answer:
    def __init__(self, answer: str, is_correct: bool, message: str):
        self.answer = answer
        self.is_correct = is_correct
        self.message = message




class QuestionGenerator:
    def __init__(self):
        self.sparql = SPARQLWrapper("https://dbpedia.org/sparql")
        self.possiple_questions = {}

    def generate_question(self, question_type=None):
        if question_type:
            return self.possible_questions[question_type]
        else:
            return choice(self.possible_questions.values())

    def _query_and_format(self, n_alternatives=4):
        # Comment
        query = self.sparql.setQuery(query_string)

        # Converts to JSON format
        self.sparql.setReturnFormat(JSON)
    
        # The returned data from the query:
        results = self.sparql.queryAndConvert()

        # The object level where the interesting data is:
        data = results["results"]["bindings"]

        shuffle(data)

        # Limits the result to n alternatives:
        return data[0:n_alternatives]

class CountryQuestionGenerator(QuestionGenerator):

    def __init__(self):
        super(self).__init__()
        self.possible_questions = {
            "capital": self.get_capital_question(),
            "population": self.get_population_question()
        }

    def generate_capital_question(self):
        query_string = 
            """
                SELECT ?country ?capital 
                WHERE {
                    ?country dbo:capital ?capital .
                    ?country dbo:countryCode ?code .
                    FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                }
            """