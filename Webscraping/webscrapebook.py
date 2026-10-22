import requests
from bs4 import BeautifulSoup  ##to get the content of the webpage in a structured way
base_url = "http://books.toscrape.com/index.html"
home_page = requests.get(base_url)
print(home_page.status_code)
from bs4 import BeautifulSoup
soup = BeautifulSoup(markup=home_page.content, parser="html.parser")
books = soup.find_all(name="li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
len(books)
books[1]
books[0:2]