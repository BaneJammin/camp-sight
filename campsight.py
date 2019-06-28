import requests, bs4, datetime
from campsightconfig import base_url, loc
from collections import OrderedDict

def build_params():
    prompts = ['month', 'day', 'year']
    params = {}
    for p in prompts:
        params[p] = int(input(f'{p.capitalize()}? '))
    stay = int(input('Nights to stay? '))
    edate = datetime.date(params['year'], params['month'], params['day']) + datetime.timedelta(days=stay)
    for p in prompts:
        params[f'e{p}'] = getattr(edate, p)
    params['find_pk'] = 1
    return params

def make_websoup():
    params = build_params()
    res = requests.get(base_url, params=params)
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    return soup

def make_filesoup(file):
    with open(file) as f:
        soup = bs4.BeautifulSoup(f.read(), features='html.parser')
    return soup

def find_available():
    avail = []
    for i in soup.find_all('table'):
        rows = i.find_all('tr')
        name = rows[0].td.text[:rows[0].td.text.find(':')]
        status = rows[2].find_all('td')[1].text
        if status == ' Reserve now':
            avail.append(name)
    return avail

#soup = make_filesoup('parks.html')
soup = make_websoup()
print(find_available())
