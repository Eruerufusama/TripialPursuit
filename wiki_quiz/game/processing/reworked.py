from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
from random import shuffle, choice
from queries import countrie_sqarql_querys
from pprint import pprint
from json import dump
from os import path, getcwd
from datatypes import Question, Answer





class QuestionGenerator:
    def __init__(self):
        self.sparql = SPARQLWrapper("https://dbpedia.org/sparql")
        self.possible_questions = {}


    def query_to_json(self):
        for query_name in countrie_sqarql_querys:
            current_data = self._query_and_format(countrie_sqarql_querys[query_name])
            with open(f"{getcwd()}\\wiki_quiz\\game\\json_data\\{query_name}.json", "w") as f:
                dump(current_data, f, indent=4)


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


if __name__ == "__main__":
    question_generator = QuestionGenerator()