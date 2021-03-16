from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
from random import shuffle, choice
from queries import countries
from pprint import pprint


import os
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)


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
        self.possible_questions = {}


    def generate_question(self, question_type: str=None):
        if question_type:
            return self.possible_questions[question_type]
        else:
            return choice(self.possible_questions.values())


    def _query_and_format(self, query_string: str, n_alternatives: int=4):
        # Comment
        query = self.sparql.setQuery(query_string)

        # Converts to JSON format
        self.sparql.setReturnFormat(JSON)
    
        # The returned data from the query:
        results = self.sparql.queryAndConvert()

        # The object level where the interesting data is:
        data = results["results"]["bindings"]


        # Limits the result to n alternatives:
        return data


class CountryQuestionGenerator(QuestionGenerator):
    def __init__(self):
        super(self).__init__()

        self.possible_questions = {
            "capital": self.get_capital_question(),
            "population": self.get_population_question()
        }
        self.queries = country

    def get_capital_question(self):
        result = self._query_and_format(self.queries["capital"])
        shuffle(result)
        return result
