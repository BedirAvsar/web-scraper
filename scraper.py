import requests
import string
import os
from bs4 import BeautifulSoup

BASE_URL = "https://www.nature.com"
START_URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page="

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0"
}

pages = int(input())
article_type = input()

for page in range(1, pages + 1):
    page_url = START_URL + str(page)
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    folder_name = f"Page_{page}"
    os.makedirs(folder_name, exist_ok=True)

    articles = soup.find_all("article")

    for article in articles:
        type_tag = article.find("span", {"data-test": "article.type"})
        if type_tag is None or type_tag.text.strip() != article_type:
            continue

        link_tag = article.find("a", {"data-track-action": "view article"})
        if link_tag is None:
            continue

        title = link_tag.text.strip()
        title = title.translate(str.maketrans("", "", string.punctuation))
        title = title.replace(" ", "_")

        article_url = BASE_URL + link_tag.get("href")
        article_response = requests.get(article_url, headers=headers)
        article_soup = BeautifulSoup(article_response.text, "html.parser")

        body = article_soup.find("p", class_="article__teaser")
        if body is None:
            continue

        text = body.text.strip()

        file_path = os.path.join(folder_name, f"{title}.txt")
        with open(file_path, "wb") as file:
            file.write(text.encode("utf-8"))
