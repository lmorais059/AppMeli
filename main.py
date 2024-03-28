# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def get_ofertas_do_dia():
    url = 'https://www.mercadolivre.com.br/ofertas'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    id = 0
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        ofertas = []
        for oferta in soup.find_all('li', class_='promotion-item'):
            id += 1
            titulo = oferta.find('p', class_='promotion-item__title').text.strip()
            desconto = oferta.find('span', class_='promotion-item__discount-text').text.strip()
            preco = oferta.find('span', class_='andes-money-amount__fraction').text.strip()
            link = oferta.find('a', class_='promotion-item__link-container')['href']
            ofertas.append({'id': id, 'titulo': titulo, 'preco': preco, 'desconto': desconto, 'link': link})
        return ofertas
    else:
        print('Falha ao obter ofertas do Mercado Livre')
        return None

# Exemplo de uso
#ofertas = get_ofertas_do_dia()
#if ofertas:
#    for oferta in ofertas:
#        print(f"Produto: {oferta['titulo']}, Preço: {oferta['preço']}, Desconto: {oferta['desconto']} Link: {oferta['link']}")
