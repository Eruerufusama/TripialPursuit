from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
from random import shuffle, choice

class CountryQuestions:
    def __init__(self):
        self.url = "https://dbpedia.org/sparql"
        self.sparql = SPARQLWrapper(self.url)
        
        self.question_list = [
                                self.get_capital_question(),
                                self.get_population_question()
                            ]

    
    def get_random_question(self):
        return choice(self.question_list)


    def get_capital_question(self):
        question = {
            'question_text': str(),
            'answers': list(),
        }
        
        """Creates a question object for a randomly generated capitol question"""
        
        query = self.sparql.setQuery(
            """
                SELECT ?country ?capital 
                WHERE {
                    ?country dbo:capital ?capital .
                    ?country dbo:countryCode ?code .
                    FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                }
            """
        )
        
        # Converts to JSON format
        self.sparql.setReturnFormat(JSON)
        
        # The returned data from the query:
        results = self.sparql.queryAndConvert()
        
        # The object level where the interesting data is:
        data = results["results"]["bindings"]

        # Randomize the order of the returned data: (Not sure if needed as resaults might be already random)
        shuffle(data) 

        # Limits the result to 4 alternatives:
        data_4_alternatives = data[0:4]

        for i, element in enumerate(data_4_alternatives):
            # Turns wikidata link and saves the end of the link after the last / and replace underscore with space.
            country = element["country"]["value"].rsplit('/', 1)[-1].replace("_", " ")
            capital = element["capital"]["value"].rsplit('/', 1)[-1].replace("_", " ")
            if i == 0:
                question["question_text"] = "What is the capitol of {}?".format(country)
                question["answers"].append(
                                            {
                                                "text": capital,
                                                "is_correct": True,
                                                "message": "That is correct, the capitol of {} is {}".format(country, capital)
                                            }
                                        )
            else:
                question["answers"].append(
                                            {
                                                "text": capital, 
                                                "is_correct": False,
                                                "message": "That is incorrect, the capitol of {} is {}".format(country, capital)
                                            }
                                        )
        
        # Makes sure the first alternative is not all ways the correct one
        shuffle(question["answers"])

        return question


    def get_population_question(self):
        question = {
            'question_text': str(),
            'answers': list(),
        }
        
        """Creates a population question object for a randomly generated population question"""
        query = self.sparql.setQuery(
            """
                SELECT ?country ?pop 
                WHERE {
                    ?country dbo:populationTotal ?pop .
                    ?country dbo:countryCode ?code
                    FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                }
            """
        )

        # Converts to JSON format
        self.sparql.setReturnFormat(JSON)
        
        # The returned data from the query:
        results = self.sparql.queryAndConvert()
        
        # The object level where the interesting data is:
        data = results["results"]["bindings"]

        # Randomize the order of the returned data: (Not sure if needed as resaults might be already random)
        shuffle(data) 

        # Limits the result to 4 alternatives:
        data_4_alternatives = data[0:4]

        for i, element in enumerate(data_4_alternatives):
            # Turns wikidata link and saves the end of the link after the last / and replace underscore with space.
            country = element["country"]["value"].rsplit('/', 1)[-1].replace("_", " ")
            population = int(element["pop"]["value"].rsplit('/', 1)[-1].replace("_", " "))
            population_mill = str(round(population / 1000000, 3)) + " mill"
            if i == 0:
                question["question_text"] = f"What is the population of {country}?"
                question["answers"].append(
                                            {
                                                "text": population_mill,
                                                "is_correct": True,
                                                "message": f"That is correct, the population of {country} is {population_mill}"
                                            }
                                        )
            else:
                question["answers"].append(
                                            {
                                                "text": population_mill, 
                                                "is_correct": False,
                                                "message": f"That is incorrect, the population of {country} is {population_mill}"
                                            }
                                        )
        
        return question
        



if __name__ == "__main__":
    CountryQuestions = CountryQuestions()
    
    pprint(CountryQuestions.get_random_question())























"""
question = {
    'question_text': 'Which of these cities is furthest south?',
    'answers': [
        {
            'text': 'Johannesburg',
            'is_correct': False,
            "message": "That is incorrect, the capitol of x is y"
        },
            
            'text': 'Sydney',
            'is_correct': False,
            "message": "That is incorrect, the capitol of x is y"
        },
            
            'text': 'Buenos Aires',
            'is_correct': True,
            "message": "That is correct, the capitol of x is y"
        },
            
            'text': 'Santiago',
            'is_correct': False,
            "message": "That is incorrect, the capitol of x is y"
        }
    ]
}
"""