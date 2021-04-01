from sys import argv
from queries import queries
from .functions import query_sparql, format_data, dump_data

def main(query_name: str, database: str="dbpedia") -> None:

    # Get query.
    query: str = queries[query_name]

    # Perform query and get data.
    data: dict = query_sparql(query)

    # Format data.
    formatted_data = format_data(data, database)

    # Write to JSON.
    dump_data(query_name, formatted_data)


if __name__ == "__main__":
    
    if argv[2]:
        main(argv[1], argv[2])
    else:
        main(argv[1])
        