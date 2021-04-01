from SPARQLWrapper import SPARQLWrapper, JSON
from os import getcwd
from sys import argv
from json import dump

from queries import queries


def query_format_dump(query_name: str, database: str="dbpedia") -> None:

    query: str = queries[query_name]
    data: dict = query_sparql(query, database)

    dump_data(query_name, data)



def dump_data(filename: str, data: dict) -> None:
    with open(f'{getcwd()}/game/json_data/{query_name}.json', 'w') as json_file:
        dump(data, json_file, indent=4)


def query_sparql(query: str) -> dict:
    """Performs a query to a semantic database.

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
    """Formats the data given a database.

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

if __name__ == "__main__":
    
    if argv[2]:
        query_format_dump(argv[1], argv[2])
    else:
        query_format_dump(argv[1])
        