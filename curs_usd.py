import math
import requests


def func_cource_of_usd():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    response = requests.get(url)
    if response.status_code == 200:
        text = response.json()

    return str(text['Valute']['USD']['Value'])