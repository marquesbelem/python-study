import requests 
from bs4 import BeautifulSoup
import pandas as pd
from mercado_livre import MercadoLivre

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

def get_products_mercado_livre(soup):
    products = soup.find_all('li', class_='ui-search-layout__item')
    data = []
    for product in products:
        name = product.find('h3', class_='poly-component__title-wrapper').text.strip()
        if "bolsa" in name.lower() or "case" in name.lower() or "estojo" in name.lower() or "capa" in name.lower():
            continue
        if "console" in name.lower() or "valve" in name.lower() or "consola" in name.lower() or "portátil" in name.lower():
            price = product.find('span', class_='andes-money-amount__fraction').string.strip()
            link = product.find('a', class_='poly-component__title')['href']
            price = "R${:.4f}".format(float(price))
            data.append({
                'NOME': name,
                'PREÇO': price,
                'LINK': link
            })
    return data

def get_html(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,   'html.parser')
    return soup

def save_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Produtos salvos em {filename}")

mercado_livre_html = get_html("https://lista.mercadolivre.com.br/steamdeck")
mercado_livre = MercadoLivre()
products = mercado_livre.get_products(mercado_livre_html)
save_csv(products, 'steamdeck.csv')