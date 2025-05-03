class MercadoLivre: 
    def get_products(self,soup):
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