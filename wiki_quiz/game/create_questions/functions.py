from random import sample
from json import load

def get_resource_url(url: dict, query_name: str) -> str:
    """
    Removes url-syntax from resource url, keeping the relevant data.

    Args:
        url (dict): url-resource.
        query_name (str): [description]

    Returns:
        str: [description]
    """
    return url[query_name]['value'].rsplit('/', 1)[-1].replace('_', ' ')


def get_answers(filepath: str, n_answers: int, difficulty:str="normal") -> list:
    """
    Fetch <n> amount of samples from the pool of possible answers.

    Args:
        filepath (str): Filepath to json-file which contains possible answers.
        n_answers (int): number of answers.

    Returns:
        list: List of answer-samples.
    """
    with open(filepath) as json_file:
        data = load(json_file)
        if difficulty == "normal":
            return sample(data, n_answers)
        elif difficulty == "easy" or difficulty == "hard":
            split = len(data) / 2
            return sample(
                data[:split] if difficulty == "easy" 
                else data[split:], n_answers
            )
            