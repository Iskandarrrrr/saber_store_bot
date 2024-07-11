import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def pars_saber(category):
    load_dotenv()
    list_saber = []
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', class_='col-12 col-sm-6 col-lg-4')

    for block in blocks[:5]:
        images = block.find('img').get('src')
        title = block.find('h4').get_text()
        price = block.find('span').get_text()
        link = HOST + block.find('a').get('href')

        list_saber.append({
            'images': images,
            'title': title,
            'price': price,
            'link': link
        })

    return list_saber



pars_saber('category/49/')
