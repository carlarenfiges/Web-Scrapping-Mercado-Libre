import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd

r = requests.get('https://listado.mercadolibre.com.ar/computacion/pc-escritorio/pc/#menu=categories')
soup = BeautifulSoup(r.content, 'html.parser')

titulos = soup.find_all('p', attrs={"class":"ui-recommendations-card__title"})
titulos = [i.text for i in titulos]

urls = soup.find_all('a', attrs={"class":"ui-recommendations-card__link"})
urls = [i.get('href') for i in urls]

dom = etree.HTML(str(soup))
precios = dom.xpath('//div[@class="ui-recommendations-card ui-recommendations-card--vertical show-original-price __item"]//div[contains(@class,"ui-recommendations-card__price-and-discount")]//span[@class="andes-money-amount ui-recommendations-card__price andes-money-amount--cents-superscript andes-money-amount--compact"]/span[2] | //div[@class="ui-recommendations-card ui-recommendations-card--vertical __item"]//div[contains(@class,"ui-recommendations-card__price-and-discount")]//span[@class="andes-money-amount ui-recommendations-card__price andes-money-amount--cents-superscript andes-money-amount--compact"]/span[2]')
precios = [i.text for i in precios]

df = pd.DataFrame({"titulos":titulos,"urls":urls,"precios":precios  })
df.to_csv('pc_mercado_libre.csv')

print(df)