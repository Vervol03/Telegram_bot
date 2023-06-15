import requests
from bs4 import BeautifulSoup

def random_mem():
    response = requests.get("https://www.anekdot.ru/random/mem/")

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        img_tags = soup.find_all("img")
        if len(img_tags) >= 5:
            return img_tags[4]["src"]