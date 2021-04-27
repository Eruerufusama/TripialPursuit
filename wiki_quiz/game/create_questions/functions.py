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
            return sample(data, n_answers)

        elif difficulty == "easy" or difficulty == "hard":
            middle = len(data) / 2
            data = data[:middle] if difficulty == "easy" else data[middle:]

            return sample(data, n_answers)


def get_samples_no_dupe(data: dict, n_answers: int) -> list:
    "Makes sure no question has duplicate URI"

    """
    alternatives = []
    uri_log = []
    
    while len(alternatives) < 4:
        current_sample = sample(data, 1)
        uri = current_sample[0]["year"]["value"]
        if uri not in uri_log and current_sample not in alternatives:
            alternatives.append(current_sample)
            uri_log.append(uri)     
    return alternatives
    """

    alternatives = []
    uri_log = []
    
    while len(alternatives) < 4:
        current_sample = sample(data, 1)
        for element in current_sample:
            for key, value in element.items():
                uri = element[key]["value"]
                if uri not in uri_log and current_sample not in alternatives:
                    alternatives.append(current_sample)
                    uri_log.append(uri)
                break
    
    for i, element in enumerate(alternatives): 
        alternatives[i] = element[0]
    
    #print("uri_log")
    #print(uri_log, "\n"*5)    
    return alternatives
    #return alternatives, uri_log


if __name__ == "__main__":
    """
    while True:
        alternatives, uri_log = get_answers("D:\\Backup\\Code\\INFO216\\Semester oppgave\\TripialPursuit\\wiki_quiz\\game\\json_data\\release_year.json", n_answers=4, difficulty="normal")
        for element in uri_log:
            print(element, uri_log.count(element))
            if uri_log.count(element) > 1:
                print(alternatives, "\n"*10, uri_log)
    """
