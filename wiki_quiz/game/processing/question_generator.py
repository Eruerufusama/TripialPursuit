from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
from random import shuffle, choice, sample
from pprint import pprint
from json import dump, load
from os import path, getcwd
from hashlib import md5
from time import sleep
from .data_types import Question, Answer
from .queries import countrie_sqarql_querys

def query_and_format(query: str, database: str) -> dict:
    sparql_wrapper = SPARQLWrapper("https://dbpedia.org/sparql")
    sparql_wrapper.setQuery(query)
    sparql_wrapper.setReturnFormat(JSON)

    result = sparql_wrapper.queryAndConvert()

    if database == "dbpedia":
        return result["results"]["bindings"]
    if database == "wikidata":
        return result

