from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


search_url = "https://www.gutenberg.org/ebooks/authors/search/?query="
base_url = "https://www.gutenberg.org"
author = ['mark twain']

def mainloop():
    html = urlopen(search_url + author[0].replace(' ','+')).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    author_url = soup.find_all("a", {"class": "link", "href": re.compile("^/ebooks/author/")})[0]

    html = urlopen(base_url + author_url['href']).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    books = soup.find_all("li", {"class": "booklink"})
    book_url = books[0].a['href']

    html = urlopen(base_url + book_url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    download = soup.find_all("a", {"class": "link", 'type':"text/plain; charset=utf-8"})

    print(urlopen(base_url + download[0]['href']).read().decode('utf-8'))

if __name__ == '__main__':
    mainloop()
    print("ok")
