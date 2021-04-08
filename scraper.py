import urllib
import urllib.request
import requests
from bs4 import BeautifulSoup
import bs4
import pandas
def get_doviz():
	url = "https://www.doviz.com/"
	sayfa = requests.get(url)
	corba = BeautifulSoup(sayfa.content,"html.parser")
	linkler = corba.findAll("span", {"class": "value"})
	kurlar = [kur.text for kur in linkler]
	degerler=["altın", "dolar", "euro", "sterlin", "bist", "BTC", "Gümüş", "Faiz"]
	s = pandas.Series(kurlar, degerler)
	return s.to_string()

print(get_doviz())
