from bs4 import BeautifulSoup
import json
import os

def makeJson(html):
    soup = BeautifulSoup(html, 'html.parser')
    postTitle = soup.select('div.catalogue > a')

    data = {}

    for title in postTitle:
        data[title.select('h1')[0].text] = title.get('href')

    return data

def makeJsonFile(data):
    with open(os.path.join('/Users/sangyeon/workspace/webCrawler', 'result.json'), 'w+') as json_file:
        json.dump(data, json_file)