from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
from random import shuffle, choice, sample
from pprint import pprint
from json import dump, load
from os import path, getcwd
from hashlib import md5
from time import sleep
try:
    from data_types import Question, Answer
    from queries import countrie_sqarql_querys
except:
    from .data_types import Question, Answer
    from .queries import countrie_sqarql_querys


class QuestionGenerator:
    def __init__(self):
        self.sparql = SPARQLWrapper("https://dbpedia.org/sparql")

    def get_url_resource(self, element: dict, key: str):
        """
        Args:
            element (dict): query data
            key (str): dict key

        Returns:
            str: name of the url resource
        """
        return element[key]["value"].rsplit('/', 1)[-1].replace("_", " ")

    def query_to_json(self):
        for query_name in countrie_sqarql_querys:
            current_data = self._query_and_format(countrie_sqarql_querys[query_name])
            with open(f"{getcwd()}\\wiki_quiz\\game\\json_data\\{query_name}.json", "w") as f:
                dump(current_data, f, indent=4)


    def _query_and_format(self, query_string: str):
        """
        Args:
            query_string (str): query in string format

        Returns:
            dict: Returns all the relevant data from a SPARQL query as a dictionary
        """

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
    

    def get_alternatives(self, file_path: str, number_of_alternatives=4):
        """
        Args:
            file_path (str): json folder location file path
            number_of_alternatives ([type], optional): [description]. Defaults to 4:int.

        Returns:
            list: returns a list with the 4 alternatives for the generated question.
        """
        with open(file_path, "r") as capital_json_data:
            data = load(capital_json_data)
            data_4_alternatives = sample(data, number_of_alternatives)
        return data_4_alternatives


class CountryQuestionGenerator(QuestionGenerator):
    def __init__(self):
        super().__init__()
        self.file_path = "\\wiki_quiz\\game\\json_data\\"
        self.possible_country_questions = [
                                            self.get_capital_question,
                                            self.get_population_question,
                                            self.get_island_question,
                                            self.get_olymics_question
                                        ]
        self.previous_questions = []


    def generate_country_questions(self, number_of_questions: int):
        """
        Args:
            number_of_questions (int): number of country category questions to generate.

        Returns:
            list: returns a list with all the n number of generated questions from the country category.
        """
        generated_questions = []
        while len(generated_questions) < number_of_questions:
            
            random_question = choice(self.possible_country_questions)()
            question_text = random_question.question
            
            if question_text not in self.previous_questions:
                generated_questions.append(random_question)
                self.previous_questions.append(question_text)
            sleep(1)
            print(self.previous_questions)
        
        return generated_questions


    def get_capital_question(self):
        """
        Returns:
            obj: returns an object which contains all the relevant data 
                 for the capital question to be desplayed on the webpage.
        """
        full_file_path = f"{getcwd()}{self.file_path}capital.json"
        data_4_alternatives = self.get_alternatives(full_file_path)

        alternatives = []
        for i, element in enumerate(data_4_alternatives):
            # Turns wikidata link and saves the end of the link after the last / and replace underscore with space.
            country = self.get_url_resource(element, "country")
            capital = self.get_url_resource(element, "capital")
            
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
        
        shuffle(alternatives)   
        question = Question(question_txt, alternatives)
        return question


    def get_population_question(self):
        full_file_path = f"{getcwd()}{self.file_path}population.json"
        data_4_alternatives = self.get_alternatives(full_file_path)

        alternatives = []

        for i, element in enumerate(data_4_alternatives):
            country = self.get_url_resource(element, "country")
            population = int(self.get_url_resource(element, "population"))
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
        
        shuffle(alternatives)
        question = Question(question_txt, alternatives)
        return question
    

    def get_island_question(self):
        full_file_path = f"{getcwd()}{self.file_path}island.json"
        data_4_alternatives = self.get_alternatives(full_file_path)

        alternatives = []
        for i, element in enumerate(data_4_alternatives):
            country = self.get_url_resource(element, "country")
            island = self.get_url_resource(element, "island")
            
            if i == 0: 
                question_txt = f"What country is the island {island} located in?"
                alternatives.append(
                    Answer(
                        country,
                        True,
                        f"That is correct, the island {island} is located in {country}"
                    )
                )
            
            else:
                alternatives.append(
                    Answer(
                        island,
                        False,
                        f"That is incorrect, the island {island} is located in {country}"
                    )
                )
        
        shuffle(alternatives)
        question = Question(question_txt, alternatives)
        return question
    
    
    def get_olymics_question(self):
        full_file_path = f"{getcwd()}{self.file_path}olympics.json"
        data_4_alternatives = self.get_alternatives(full_file_path)

        alternatives = []
        for i, element in enumerate(data_4_alternatives):
            country = self.get_url_resource(element, "country")
            olympic = self.get_url_resource(element, "olympic")
            
            if i == 0: 
                    question_txt = f"What country hosted the {olympic} olymics?"
                    alternatives.append(
                        Answer(
                            country,
                            True,
                            f"That is correct, {country} hosted the {olympic} olympics"
                        )
                    )
                
            else:
                alternatives.append(
                    Answer(
                        country,
                        False,
                        f"That is incorrect, {country} hosted the {olympic} olympics"
                    )
                )
        shuffle(alternatives)
        question = Question(question_txt, alternatives)
        return question


if __name__ == "__main__":
    question_generator = QuestionGenerator()
    question_generator.query_to_json()
    
    counrty_question_generator = CountryQuestionGenerator()
    question_list = counrty_question_generator.generate_country_questions(10)

    for question in question_list:
        #pprint(question.to_dict())
        pass
    
    pprint(counrty_question_generator.previous_questions)
    #pprint(counrty_question_generator.get_olymics_question().to_dict())