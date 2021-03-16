from SPARQLWrapper import SPARQLWrapper, JSON
import pprint

url = "https://dbpedia.org/sparql"
sparql = SPARQLWrapper(url)

# Creating the query, but does not send it.
# SELECT the 10 first triples in the graph

#sparql.setQuery("""
#    select ?movie ?runtime WHERE{
#    ?movie dbo:runtime ?runtime
#    } LIMIT(20)
#""")


sparql.setQuery("""
    SELECT ?country ?capital WHERE{
    ?country dbo:capital ?capital.
    ?country dbo:countryCode ?code .
} LIMIT(20)
""")

# Specifying a return format
sparql.setReturnFormat(JSON)

# Running the query
# The response is a QueryResult-object, whis is not really managable form python
# The convert-method fixes this
results = sparql.query().convert()
# Alternative:
results = sparql.queryAndConvert()
pprint.pprint(results)