from random import sample
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
            return get_samples_no_dupe(data, n_answers)
            #return sample(data, n_answers)
        elif difficulty == "easy" or difficulty == "hard":
            split = len(data) / 2
            return sample(
                data[:split] if difficulty == "easy" 
                else data[split:], n_answers
            )

def get_samples_no_dupe(data: dict, n_answers: int) -> list:
    "Makes sure no question has duplicate URI"

    alternatives = []
    uri_log = []
    
    while len(alternatives) < 4:
        current_sample = sample(data, 1)
        for element in current_sample:
            for key, value in element.items():
                uri = element[key]["value"]
                if uri not in uri_log:
                    print(uri_log)
                    alternatives.append(current_sample)
                    uri_log.append(uri)     
    return alternatives


if __name__ == "__main__":
    pprint(get_answers("D:\\Backup\\Code\\INFO216\\Semester oppgave\\TripialPursuit\\wiki_quiz\\game\\json_data\\capital.json", n_answers=4, difficulty="normal"))