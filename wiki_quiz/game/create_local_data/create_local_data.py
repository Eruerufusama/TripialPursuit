from sys import argv
from queries import queries
from functions import query_sparql, format_data, dump_data

def main(query_name: str, database: str="dbpedia") -> None:

    # USES JSON-FILE
    query: str = queries[query_name]

    # USES DATABASE INSTEAD
    # query: str = Query.objects.filter(name=query_name).first().query

    # Perform query and get data.
    data: dict = query_sparql(query, database)

    # Format data.
    formatted_data = format_data(data)

    # Write to JSON.
    dump_data(query_name, formatted_data)


if __name__ == "__main__":
    # Input the name of the query from queries.py and select the correct database:
    query_name = input("name: ")
    db = input("Database (wikidata/dbpedia): ")
    main(query_name, db)