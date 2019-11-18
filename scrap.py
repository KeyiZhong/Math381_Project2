from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
import os.path
import fnmatch


search_url = "https://www.gutenberg.org/ebooks/authors/search/?query="
base_url = "https://www.gutenberg.org"
author = ['mark twain']


def downloadPage(books):
    for i in range(len(books)):
        book_url = books[i].a['href']

        html = urlopen(base_url + book_url).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')
        name = soup.find('h1').contents[0]
        download = soup.find_all("a", {"class": "link", 'type': re.compile("^text/plain")})
        if not name.contains("Gutenberg"):
            if not os.path.exists(author[0]):
                os.makedirs(author[0])

            file_exist = False
            for file in os.listdir(author[0] + "/"):
                if fnmatch.fnmatch(file, name.replace(' ', '_')[0:10] + "*"):
                    print(name)
                    file_exist = True

            if len(download) != 0 and not file_exist:
                try:
                    f = open(author[0] + "/" + name.replace(' ', '_') + ".txt", "w+")
                    f.write(urlopen(base_url + download[0]['href']).read().decode('utf-8'))
                    f.close()
                except:
                    print(name)


def mainloop():
    # search author
    for i in range(len(author)):
        html = urlopen(search_url + author[i].replace(' ','+')).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')
        author_url = soup.find_all("a", {"class": "link", "href": re.compile("^/ebooks/author/")})[0]

        # select author
        html = urlopen(base_url + author_url['href']).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')
        books = soup.find_all("li", {"class": "booklink"})
        # download first page
        downloadPage(books)
        nextpage = soup.find("a", {'title': 'Go to the next page of results.'})
        while nextpage:
            html = urlopen(base_url + nextpage['href']).read().decode('utf-8')
            soup = BeautifulSoup(html, features='lxml')
            books = soup.find_all("li", {"class": "booklink"})
            downloadPage(books)
            nextpage = soup.find("a", {'title': 'Go to the next page of results.'})


if __name__ == '__main__':
    mainloop()
    print("ok")
