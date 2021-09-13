import requests
import time
from bs4 import BeautifulSoup


url = 'https://ethereumprice.org/'
response = requests.get(url)
html = response.text

scrap = BeautifulSoup(html, 'html.parser')

price_input_el = scrap.find('input', class_="js--converter-quote")
price_in_dollars = float(price_input_el.get('value'))
print(time.time(), 'The etherium price is', price_in_dollars)
