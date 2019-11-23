from bs4 import BeautifulSoup
from urllib.request import urlopen


def extract(page):
    if type(page) == str:
        page = urlopen(page)
    text = BeautifulSoup(page).get_text()
    return text.replace("\n", "").replace("\t", "")
