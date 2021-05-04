# !!! This was made as a proof of concept to test how a dynamic query would work!!!

# !!! The resault of the query only work for some topics due to data incosistancy 
# !!! and lack of structure on wikidata!!!

# !!! Topics we recomend to test are Ronaldo, Donald Trump !!!

# !!! Due to the poor resault of the generated questions we decided to not implement
# !!! this code into the final project interfance


import re
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from pprint import pprint
import re
from random import choice
from SPARQLWrapper import SPARQLWrapper, JSON
from data_types import Question, Answer

def get_q_code(search: str, n_searches: int):
    """Lets you search for a ting in wikidata and returns 4 search resaults

    Args:
        search (str): search string
        n_searches (int): number of search resaults you want back

    Returns:
        [type]: returns a list of data from the search
    """
    url = "https://www.wikidata.org/w/index.php?search=" + search
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")

    search_data = []

    searchresults = bs.find("div", {"class": "searchresults"}).find_all("a")
    for i, result in enumerate(searchresults):
        if i < n_searches:
            q_code = result["href"].split("/")[-1]
            title = result["title"].replace("\u200e", "")
            search_data.append([q_code, title])
            continue
        return search_data

def print_search(search_result: list):
    """Shoiws the data from get_q_code

    Args:
        search_result (list): data the print will show
    """

    for i, element in enumerate(search_result):
        print(f"{i} = {element[1]}")


def select_search(search_result: list, index: int):
    """returns the selected search resault from and index

    Args:
        search_result (list): search resault data
        index_int (int): index number of selected data from search

    Returns:
        [str]: q_code string
    """
    return search_result[index][0]


def extract_usefull_properties(q_code: str) -> list:
    """ extracts all the usefull properties we can use to generate a query from scraping
        which are from the statements category "https://www.wikidata.org/wiki/Q11571"


    Args:
        q_code (str): string of the searched q_code

    Returns:
        p_codes (list): all the usefull p_codes to generate a query
    """
    
    url = "https://www.wikidata.org/wiki/" + q_code
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    table_data = bs.find("div", {"class": "wikibase-listview"})

    p_codes = []
    for element in table_data:
        current_p_code = element.get("data-property-id")
        p_codes.append(current_p_code)
    return p_codes


def get_property_name(prop):
    url = "https://www.wikidata.org/wiki/Property:" + prop
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    h1 = bs.find("h1")
    property_name = h1.find("span", {"class": "wikibase-title-label"})
    return property_name.get_text()


def query_sparql(query: str, database: str) -> dict:
    """
    Performs a query to a semantic database.

    Args:
        query (str): SPARQL query.

    Returns:
        dict: raw data from a given query.
    """

    sparql_wrapper = SPARQLWrapper(f'https://{"query." if database == "wikidata" else ""}{database}.org/sparql')
    sparql_wrapper.setQuery(query)
    sparql_wrapper.setReturnFormat(JSON)
    data = sparql_wrapper.queryAndConvert()
    return data['results']['bindings']


def create_undefined_question(query_data: dict, property_name: str):
    """ 
        Structures the data in question format and displays it.
    Args:
        query_data (dict): the returened data from the query
        property_name (str): the property from the type we seached for. 
    """
    
    correct_subject = query_data[0]["personLabel"]["value"]
    del query_data[0]["personLabel"]

    correct_object = query_data[0]["valueLabel"]["value"]
    del query_data[0]["valueLabel"]

    alternatives = []
    for element in query_data[0]:
        alternatives.append(query_data[0][element]["value"])
    
    question_text = f"{correct_subject} {property_name} _______?"

    print(question_text)
    print("correct:", correct_object)
    print("alternatives:", alternatives)

    


if __name__ == "__main__":
    search = input("Type what to search for on wikidata:\n").replace(" ", "")
    search_result = get_q_code(search, 4)
    
    print_search(search_result)
    index = int(input("select index:\n"))
    
    q_code = select_search(search_result, index)
    

    p_codes = extract_usefull_properties(q_code)

    selected_p_code = choice(p_codes)
    property_name = get_property_name(selected_p_code)

    query = (
        "SELECT DISTINCT ?personLabel ?valueLabel ?value2Label ?value3Label ?value4Label WHERE {"
        "SERVICE wikibase:label {bd:serviceParam wikibase:language '[AUTO_LANGUAGE],en'.}"
        "{SELECT ?person ?value ?value2 ?value3 ?value4 WHERE{"
            f"Filter(?person = wd:{q_code}) ."
            "?person wdt:P31 ?type;"
                    f"wdt:{selected_p_code} ?value."
            "?person2 wdt:P31 ?type;"
                    f"wdt:{selected_p_code} ?value2."
            "?person3 wdt:P31 ?type;"
                    f"wdt:{selected_p_code} ?value3."
            "?person4 wdt:P31 ?type;"
                    f"wdt:{selected_p_code} ?value4."
            "Filter(?value != ?value2)"
            "Filter(?value != ?value3)"
            "Filter(?value != ?value4)"
            "Filter(?value3 != ?value2)"
            "Filter(?value4 != ?value2)"
            "Filter(?value3 != ?value4)"
        "} LIMIT 1}"
    "}"
    )
    
    query_data = query_sparql(query, "wikidata")
    create_undefined_question(query_data, property_name)