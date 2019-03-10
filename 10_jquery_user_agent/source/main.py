import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))