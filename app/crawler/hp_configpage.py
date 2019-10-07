from bs4 import BeautifulSoup
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def hp_configpage(ip):
    url = 'http://{}/SSI/info_configuration.htm'.format(ip)
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.findAll('table')
    data = data[5].find("td", {"class": "itemFont"})
    return data.contents[0]
