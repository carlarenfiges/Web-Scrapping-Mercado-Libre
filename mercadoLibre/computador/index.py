import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd

r = requests.get('https://listado.mercadolibre.com.ar/computador#D[A:computador]')
soup = BeautifulSoup(r.content, 'html.parser')

titulos = soup.find_all('h2', attrs={"class":"ui-search-item__title"})
titulos = [i.text for i in titulos]
print(len(titulos))

urls = soup.find_all('a', attrs={"ui-search-item__group__element ui-search-link__title-card ui-search-link"})
urls = [i.get('href') for i in urls]
print(len(urls))

dom = etree.HTML(str(soup))
precios = dom.xpath('//li[@class="ui-search-layout__item shops__layout-item ui-search-layout__stack"]//div[@class="ui-search-result__content-columns"]//div[@class="ui-search-result__content-column ui-search-result__content-column--left"]//div[1]/div//div[@class="ui-search-price__second-line"]//span[@class="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript"]/span[2] ')
precios = [i.text for i in precios]
print(len(precios))

siguiente = dom.xpath('//div[@class="ui-search"]//ul/li[contains(@class,"--next")]/a ')[0].get('href')
print(siguiente)

#ini = int(soup.find('button', attrs={"andes-pagination__link"}).text)
ini = 0
cant = soup.find_all('button', attrs={"andes-pagination__link"})
ult = cant[-1].text

lista_titulos = []
lista_urls = []
lista_precios = []

siguiente = 'https://listado.mercadolibre.com.ar/computador#D[A:computador]'
while True:
    if siguiente: 
        r = requests.get(siguiente)
        if r.status_code==200:
            soup = BeautifulSoup(r.content, 'html.parser')
            # TITULOS
            titulos = soup.find_all('h2', attrs={"class":"ui-search-item__title"})
            titulos = [i.text for i in titulos]
            lista_titulos.extend(titulos)
            # URLS
            urls = soup.find_all('a', attrs={"ui-search-item__group__element ui-search-link__title-card ui-search-link"})
            urls = [i.get('href') for i in urls]
            lista_urls.extend(urls)
            # PRECIOS
            dom = etree.HTML(str(soup))
            precios = dom.xpath('//li[@class="ui-search-layout__item shops__layout-item ui-search-layout__stack"]//div[@class="ui-search-result__content-columns"]//div[@class="ui-search-result__content-column ui-search-result__content-column--left"]//div[1]/div//div[@class="ui-search-price__second-line"]//span[@class="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript"]/span[2] ')
            precios = [i.text for i in precios]
            lista_precios.extend(precios)

            #ini = int(soup.find('button', attrs={"andes-pagination__link"}).text)
            ini = ini + 1
            cant = soup.find_all('button', attrs={"andes-pagination__link"})
            ult = cant[-1].text
        else:
            break
        print(ini,ult)
        if ini==ult:
            break
        siguiente = dom.xpath('//div[@class="ui-search"]//ul/li[contains(@class,"--next")]/a ')[0].get('href')
    else: 
        break

min_length = min(len(lista_titulos), len(lista_urls), len(lista_precios))
lista_titulos = lista_titulos[:min_length]
lista_urls = lista_urls[:min_length]
lista_precios = lista_precios[:min_length]

df = pd.DataFrame({"titulos":lista_titulos,"urls":lista_urls,"precios":lista_precios  })
df.to_csv('computador_mercado_libre.csv')
