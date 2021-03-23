from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
from random import shuffle, choice, sample
from pprint import pprint
from json import dump, load
from os import path, getcwd
# from data_types import Question, Answer
# from queries import countrie_sqarql_querys
from .data_types import Question, Answer
from .queries import countrie_sqarql_querys


class QuestionGenerator:
    def __init__(self):
        self.sparql = SPARQLWrapper("https://dbpedia.org/sparql")


    def query_to_json(self):
        for query_name in countrie_sqarql_querys:
            current_data = self._query_and_format(countrie_sqarql_querys[query_name])
            with open(f"{getcwd()}\\wiki_quiz\\game\\json_data\\{query_name}.json", "w") as f:
                dump(current_data, f, indent=4)


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
    

    def get_4_alternatives(self, file_path: str):
        with open(file_path, "r") as capital_json_data:
            data = load(capital_json_data)
            data_4_alternatives = sample(data, 4)
        return data_4_alternatives


class CountryQuestionGenerator(QuestionGenerator):
    def __init__(self):
        super().__init__()
        self.file_path = "\\wiki_quiz\\game\\json_data\\"
        self.possible_country_questions = [
                                            self.get_capital_question(),
                                            self.get_population_question()
                                        ]


    def generate_country_questions(self, number_of_questions: int):
        generated_questions = []
        for i in range(number_of_questions):
            random_question = choice(self.possible_country_questions)
            generated_questions.append(random_question)
        return generated_questions


    def get_capital_question(self):
        full_file_path = f"{getcwd()}{self.file_path}capital.json"
        data_4_alternatives = self.get_4_alternatives(full_file_path)

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
        shuffle(question.answers)
        return question

    def get_population_question(self):
        full_file_path = f"{getcwd()}{self.file_path}population.json"
        data_4_alternatives = self.get_4_alternatives(full_file_path)

        alternatives = []

        for i, element in enumerate(data_4_alternatives):
            country = element["country"]["value"].rsplit('/', 1)[-1].replace("_", " ")
            population = int(element["population"]["value"].rsplit('/', 1)[-1].replace("_", " "))
            population_mill = f"{str(round(population / 1000000, 3))} mill"

            if i == 0:
                question_txt = f"What is the population of {country}?"
                alternatives.append(
                    Answer(
                        population_mill,
                        True,
                        f"That is correct, the population of {country} is {population_mill}"
                    )
                )
            
            else:
                alternatives.append(
                    Answer(
                        population_mill,
                        False,
                        f"That is incorrect, the population of {country} is {population_mill}"
                    )
                )
            
        question = Question(question_txt, alternatives)
        shuffle(question.answers)
        return question



if __name__ == "__main__":
    question_generator = QuestionGenerator()
    question_generator.query_to_json()
    
    counrty_question_generator = CountryQuestionGenerator()
    question_list = counrty_question_generator.generate_country_questions(10)
    
    print(question_list)

    for obj in question_list:
        for alternative in obj.answers:
            print(f"answer: {alternative.answer}, is correct: {alternative.is_correct}, message: {alternative.message}\n")