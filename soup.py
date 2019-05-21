from bs4 import BeautifulSoup
import requests
import csv

url = 'http://www.cmfchile.cl/institucional/mercados/entidad.php?auth=&send=&mercado=V&rut=9383&grupo=&tipoentidad=FIRES&vig=VI&row=AAAw+cAAhAABP4PAAC&control=svs&pestania=1'

source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')

print(soup)