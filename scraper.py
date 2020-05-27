from bs4 import BeautifulSoup
import requests

# <tr>
# <td style="font-weight: bold; font-size:16px; text-align:left; padding-left:5px; padding-top:10px; padding-bottom:10px">United States</td>
# <td style="font-weight: bold; text-align:right">1,736,744</td>
# <td style="font-weight: bold; text-align:right">101,470</td>
# <td style="font-size:14px; color:#aaa; text-align:right">North America</td>
# </tr>

def scrape():
    res = requests.request("GET",url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/')
    soup = BeautifulSoup(res.content, 'html5lib')
    data = list()
    table = soup.find('table', attrs={'id':'table3'})
    table = table.find('tbody')
    id = 0
    for row in table.find_all('tr'):
        c = 0
        d = dict()
        d['_id'] = id
        for element in row.find_all('td'):
            if c==0:
                d['country'] = element.text
            if c==1:
                d['cases'] = element.text
            if c==2:
                d['deaths'] = element.text
            if c==3:
                d['region'] = element.text
            c = c + 1
        data.append(d)
        id = id + 1
    return data

def debug(data):
    for i in data:
        print(i)

if __name__ == "__main__":
    debug(scrape())