from bs4 import BeautifulSoup
import requests


def get_rate(country1,country2):
    url=f'https://www.x-rates.com/calculator/?from={country1}&to={country2}&amount=1'
    contents=requests.get(url).text
    #print(contents.text)
    parse=BeautifulSoup(contents,'html.parser')
    rate=parse.find("span",class_="ccOutputRslt").get_text()
    print(rate[:-4])

get_rate('USD','EUR')