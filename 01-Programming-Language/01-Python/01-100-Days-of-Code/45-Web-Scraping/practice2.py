import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
page = response.text

soup = BeautifulSoup(page,"html.parser")

# article_text = soup.find(name="span",class_="titleline").getText()
# article_link = soup.find(name="span",class_="sitestr").getText()
# article_upvote = soup.find(name="span",class_="score").getText()

# print(article_link)
# print(article_upvote)

# print(soup.find_all(name="span",class_="titleline"))
article_texts = [text.getText() for text in soup.find_all(name="span",class_="titleline")]
article_links = [text.getText() for text in soup.find_all(name="span",class_="sitestr")]
article_upvotes = [int(text.getText().split()[0]) for text in soup.find_all(name="span",class_="score")]

max_upvote = max(article_upvotes)
idx = article_upvotes.index(max_upvote)

print(article_texts[idx])
print(article_links[idx])
print(article_upvotes[idx])
