import re
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from pprint import pprint
import re


def get_q_code(search, n_searches):
    url = "https://www.wikidata.org/w/index.php?search=" + search
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")

    search_data = []

    searchresults = bs.find("div", {"class": "searchresults"}).find_all("a")
    for i, result in enumerate(searchresults):
        if i < n_searches:
            q_code = result["href"].split("/")[-1]
            title = result["title"].replace("\u200e", "")
            search_data.append([q_code, title])
            continue
        return search_data


def print_search(search_result):
    for i, element in enumerate(search_result):
        print(f"{i} = {element[1]}")

def select_search(search_result, index):
    return search_result[index][0]

def extract_usefull_properties():
    pass

if __name__ == "__main__":
    search = input("Type what to search for on wikidata\n")
    search_result = get_q_code(search, 4)
    print_search(search_result)
    index = int(input("select index\n"))
    q_code = select_search(search_result, index)
    