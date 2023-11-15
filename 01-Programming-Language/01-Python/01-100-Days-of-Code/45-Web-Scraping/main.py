import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
page = response.text
soup = BeautifulSoup(page,"html.parser")

movielist = [title.getText() for title in soup.find_all(name="h3",class_="title")]
# movielist = sorted(movielist,)
movielist.reverse()

with open("01-Programming-Language\\01-Python\\01-100-Days-of-Code\\45-Web-Scraping\\movielist.txt","w") as file:
    for movie in movielist:
        try:
            file.write(f"{movie}\n")
        except:
            file.write(f"{movie.encode('UTF-8')}\n")