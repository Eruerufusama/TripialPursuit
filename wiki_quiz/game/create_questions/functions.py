from random import sample
from json import load

def get_resource_url(query_data: dict, key: str) -> str:
    return query_data[key]['value'].rsplit('/', 1)[-1].replace('_', ' ')


def get_answers(filepath: str, n_answers: int) -> list:
    with open(filepath) as json_file:
        return sample(load(json_file), n_answers)