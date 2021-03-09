from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
from random import shuffle, choice

class CountryQuestions:
    def __init__(self):
        self.url = "https://dbpedia.org/sparql"
        self.sparql = SPARQLWrapper(self.url)
        self.question = {
            'question_text': str(),
            'answers': list(),
        }
        self.question_list = [self.capital_question()]

    def get_random_question(self):
        return choice(self.question_list)

    def capital_question(self):
        """Creates a question object for a random capitol question"""
        
        query = self.sparql.setQuery("""
            SELECT ?country ?capital WHERE {
                ?country dbo:capital ?capital .
                ?country dbo:countryCode ?code .
                FILTER NOT EXISTS {?country dbp:dateEnd ?date}
            }
        """)
        
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
                self.question["question_text"] = "What is the capitol of {}?".format(country)
                self.question["answers"].append(
                                                {
                                                    "text": capital,
                                                    "is_correct": True,
                                                    "message": "That is correct, the capitol of {} is {}".format(country, capital)
                                                }
                                            )
            else:
                self.question["answers"].append(
                                                {
                                                    "text": capital, 
                                                    "is_correct": False,
                                                    "message": "That is incorrect, the capitol of {} is {}".format(country, capital)
                                                }
                                            )
        
        # Makes sure the first alternative is not all ways the correct one
        shuffle(self.question["answers"])

        return self.question


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
            "message": "That is correct, the capitol of x is y"
        },
            
            'text': 'Sydney',
            'is_correct': False,
            "message": "That is correct, the capitol of x is y"
        },
            
            'text': 'Buenos Aires',
            'is_correct': True,
            "message": "That is correct, the capitol of x is y"
        },
            
            'text': 'Santiago',
            'is_correct': False,
            "message": "That is correct, the capitol of x is y"
        }
    ]
}
"""