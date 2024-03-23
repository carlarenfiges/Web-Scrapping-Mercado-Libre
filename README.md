# Proyecto de Web Scraping

Este proyecto consta de varios scripts en Python diseñados para extraer información de la web utilizando técnicas de web scraping. Los scripts recopilan datos de productos de computación de Mercado Libre, ya sea utilizando BeautifulSoup y lxml para analizar el HTML de las páginas web o mediante el uso de su API.
Archivos del Proyecto
# 1. pcGamer.py

Este script extrae información sobre las PC de escritorio disponibles en Mercado Libre. Recopila títulos, URLs y precios de los productos y guarda los datos en un archivo CSV llamado pc_mercado_libre.csv.

# 2. computador.py

Este script recopila información sobre los computadores disponibles en Mercado Libre. Al igual que el anterior, extrae títulos, URLs y precios de los productos, y guarda los datos en un archivo CSV llamado computador_mercado_libre.csv.

# 3. computadorAPI.py

Este script implementa una API simple utilizando Flask. Proporciona endpoints para acceder a los datos recopilados sobre productos de computación en Mercado Libre.
Funciones Auxiliares (functions.py)

Este archivo contiene funciones auxiliares utilizadas en los scripts de web scraping. Incluye funciones para recopilar todos los productos disponibles o para limitar el número de productos extraídos según una cantidad específica.

## Uso

1. pcGamer.py:

Este script recopila datos sobre PC de escritorio y guarda los resultados en pc_mercado_libre.csv.

2. computador.py:

Este script recopila datos sobre computadores y guarda los resultados en computador_mercado_libre.csv.

3. computadorAPI.py:

Este script inicia la API que proporciona acceso a los datos sobre productos de computación.

## Dependencias

    requests
    BeautifulSoup
    lxml
    pandas
    Flask
