from random import choice, shuffle
from json import load
from pprint import pprint

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


def get_answers(filepath: str, n_answers: int, difficulty: str="normal") -> list:
    """
    Fetch <n> amount of samples from the pool of possible answers.

    Args:
        filepath (str): Filepath to json-file which contains possible answers.
        n_answers (int): Number of answers.
        difficulty (str): Level of difficulty for answers.

    Returns:
        list: List of answer-samples.
    """
    with open(filepath) as json_file:
        data = load(json_file)

        if difficulty == "normal":
            # sample(data, 4)
            return get_samples_no_dupe(data, n_answers)

        elif difficulty == "easy" or difficulty == "hard":
            middle = len(data) / 2
            data = data[:middle] if difficulty == "easy" else data[middle:]

            return get_samples_no_dupe(data, n_answers)


def get_samples_no_dupe(data: dict, n_answers: int) -> list:
    """ Fetches for unique samples from the dataset
        and makes sure that no data can have the same value for the given key
        to prevent duplicate alternatives in the question

    Args:
        data (dict): json file data
        n_answers (int): number of alternatives

    Returns:
        list: with the n valid examples
    """
    current_chosen_alts_list = []
    shuffle(data)
    correct = choice(data)

    for current in data:
        if len(current_chosen_alts_list) == n_answers:
            return current_chosen_alts_list
        if valid_alternative(current, current_chosen_alts_list):
            current_chosen_alts_list.append(current)
    

def valid_alternative(current: dict, current_chosen_alts_list: list):
    """ Helper function for get_samples_no_dupe.
        
    Args:
        current (dict): [description]
        current_chosen_alts_list (list): [description]

    Returns:
        bool: Returns a boolian True if the values dont match
        and returns boolian false if the values match 
    """
    for key, val in current.items():
        for alt in current_chosen_alts_list:
            if alt[key]["value"] == val["value"]:
                return False
    return True


if __name__ == "__main__":
    pprint(get_answers("D:\\Backup\\Code\\INFO216\\Semester oppgave\\TripialPursuit\\wiki_quiz\\game\\json_data\\land_locked.json", n_answers=2, difficulty="normal"))