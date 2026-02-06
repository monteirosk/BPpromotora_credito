import requests
import pandas as pd
import bs4
from concurrent.futures import ThreadPoolExecutor
import json

def get_data(year):
    
    # https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2015
    
    headers = {
    'accept': '*/*',
    'cache-control': 'no-cache',
    'referer': 'https://www.scrapethissite.com/pages/ajax-javascript/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',   
    }
    params = {
        'ajax': 'true',
        'year': year,
    }

    try:
        response = requests.get('https://www.scrapethissite.com/pages/ajax-javascript/', params=params,  headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        raise ValueError("Falha no scrape")
    

def get_years():
    try:    
        response = requests.get('https://www.scrapethissite.com/pages/ajax-javascript/')
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        years = soup.find('div', class_='col-md-12 text-center')
        years = [year.text for year in years.find_all('a', class_='year-link')]
        return years
    except requests.exceptions.HTTPError:
        raise ValueError("Falha no scrape")


def get_all():
    years = get_years()
    dados = []
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        result_list = list(executor.map(get_data, years))

    for data in result_list:
        dados.extend(data)

    df = pd.DataFrame(dados)
    df['best_picture'].fillna(False, inplace=True)
    df['best_picture'] = df['best_picture'].astype(bool)
    return df

if __name__ == '__main__':
    #get_all()
    print(get_data(2015))
    