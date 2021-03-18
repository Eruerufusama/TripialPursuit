from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
from random import shuffle, choice
from queries import countrie_sqarql_querys
from pprint import pprint
from json import dump, load
from os import path, getcwd
from data_types import Question, Answer





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
        self.sparql.setQuery(query_string)

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
        super().__init__()
        self.file_path = "\\wiki_quiz\\game\\json_data\\"


    def get_capital_question(self):
        full_file_path = f"{getcwd()}{self.file_path}capital.json"
        
        with open(full_file_path, "r") as capital_json_data:
            data = load(capital_json_data)
            shuffle(data)
            data_4_alternatives = data[0:4]

            alternatives = []
            for i, element in enumerate(data_4_alternatives):
                # Turns wikidata link and saves the end of the link after the last / and replace underscore with space.
                country = element["country"]["value"].rsplit('/', 1)[-1].replace("_", " ")
                capital = element["capital"]["value"].rsplit('/', 1)[-1].replace("_", " ")
                
                if i == 0:
                    question_txt = f"What is the capitol of {country}?"
                    alternatives.append(
                        Answer(
                            capital,
                            True,
                            f"That is correct, the capitol of {country} is {capital}"
                        )
                    )
                
                else:
                    alternatives.append(
                        Answer(
                            capital,
                            False,
                            f"That is incorrect, the capitol of {country} is {capital}"
                        )
                    )
                
            question = Question(question_txt, alternatives)
                
            return question




if __name__ == "__main__":
    question_generator = QuestionGenerator()
    question_generator.query_to_json()
    
    counrty_question_generator = CountryQuestionGenerator()
    obj = counrty_question_generator.get_capital_question()
    
    print(obj.question)
    for alternative in obj.answers:
        print(f"answer: {alternative.answer}, is correct {alternative.is_correct}, message {alternative.message}\n")