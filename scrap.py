from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
import os.path
import fnmatch


search_url = "https://www.gutenberg.org/ebooks/authors/search/?query="
base_url = "https://www.gutenberg.org"
authors = ['mark twain', 'charles dickens', 'Jane Austen', 'Leo Tolstoy', 'Virginia Woolf', 'F. Scott Fitzgerald',
          'Lewis Carroll', 'Mary Shelley', 'Herman Melville', 'Oscar Wilde', 'Arthur Conan Doyle']

def downloadPage(books, author):
    for i in range(len(books)):
        book_url = books[i].a['href']

        html = urlopen(base_url + book_url).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')
        name = soup.find('h1').contents[0]
        download = soup.find_all("a", {"class": "link", 'type': re.compile("^text/plain")})
        if not name.__contains__("Gutenberg"):
            file_exist = False
            for file in os.listdir(author + "/"):
                if fnmatch.fnmatch(file, name.replace(' ', '_')[0:10] + "*"):
                    file_exist = True

            if len(download) != 0 and not file_exist:
                try:
                    f = open(author + "/" + name.replace(' ', '_') + ".txt", "w+")
                    f.write(urlopen(base_url + download[0]['href']).read().decode('utf-8'))
                    f.close()
                except:
                    os.remove(author + "/" + name.replace(' ', '_') + ".txt")
                    print(name + " not download and removed")


def mainloop():
    # search author
    for i in range(len(authors)):
        if not os.path.exists(authors[i] + " done"):
            if not os.path.exists(authors[i]):
                os.makedirs(authors[i])
            html = urlopen(search_url + authors[i].replace(' ','+')).read().decode('utf-8')
            soup = BeautifulSoup(html, features='lxml')
            author_url = soup.find_all("a", {"class": "link", "href": re.compile("^/ebooks/author/")})[0]

            # select author
            html = urlopen(base_url + author_url['href']).read().decode('utf-8')
            soup = BeautifulSoup(html, features='lxml')
            books = soup.find_all("li", {"class": "booklink"})
            # download first page
            downloadPage(books, authors[i])
            nextpage = soup.find("a", {'title': 'Go to the next page of results.'})
            while nextpage:
                html = urlopen(base_url + nextpage['href']).read().decode('utf-8')
                soup = BeautifulSoup(html, features='lxml')
                books = soup.find_all("li", {"class": "booklink"})
                downloadPage(books, authors[i])
                nextpage = soup.find("a", {'title': 'Go to the next page of results.'})
            os.rename(authors[i], authors[i] + " done")
        print("done " + authors[i])


if __name__ == '__main__':
    mainloop()
    print("ok")
