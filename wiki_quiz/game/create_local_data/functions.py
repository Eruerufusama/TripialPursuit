from SPARQLWrapper import SPARQLWrapper, JSON
from os import getcwd
from json import dump


def query_sparql(query: str) -> dict:
    """
    Performs a query to a semantic database.

    Args:
        query (str): SPARQL query.

    Returns:
        dict: raw data from a given query.
    """

    sparql_wrapper = SPARQLWrapper('https://dbpedia.org/sparql')
    sparql_wrapper.setQuery(query)
    sparql_wrapper.setReturnFormat(JSON) # Rewrite function for n3?
    return sparql_wrapper.queryAndConvert()


def format_data(data: dict, database: str) -> dict:
    """
    Formats the data given a database.

    Args:
        data (dict): query-data from a SPARQL-query.
        database (str): database from which the query was made to.

    Returns:
        dict: Properly formatted data.
    """

    if database == 'dbpedia':
        return data['results']['bindings']
    if database == 'wikidata':
        return data


def dump_data(filename: str, data: dict) -> None:
    """
    Creates a json-file with query-result.

    Args:
        filename (str): name of file to write to.
        data (dict): query-result.
    """
    
    with open(f'{getcwd()}/game/json_data/{filename}.json', 'w') as json_file:
        dump(data, json_file, indent=4)


