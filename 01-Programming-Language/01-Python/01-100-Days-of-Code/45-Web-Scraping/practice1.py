from bs4 import BeautifulSoup

with open(file="01-Programming-Language\\01-Python\\01-100-Days-of-Code\\45-Web-Scraping\\website.html",encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content,'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.p)

all_p_tag = soup.find_all(name="p")

for tag in all_p_tag:
    print(tag.getText().encode('utf-8'))

heading = soup.find(name="h1",id="name")
print(heading)

