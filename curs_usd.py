import requests
from bs4 import BeautifulSoup


def func_cource_of_usd():
    url = 'https://cbr.ru/'

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, 'html.parser')

    table = soup.findAll('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})

    count = 0
    cource_of_usd = 0
    for sum in table:
        cource_of_usd = sum.text
        count += 1
        if count == 2:
            break

    cource_of_usd_m = cource_of_usd[:7]
    cource_of_usd_m = cource_of_usd_m.replace(',', '.')
    # cource_of_usd_m = (float(cource_of_usd_m))
    return str(cource_of_usd_m)


# print(func_cource_of_usd())
