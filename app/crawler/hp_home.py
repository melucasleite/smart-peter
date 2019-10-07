from bs4 import BeautifulSoup
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def hp_home(ip):
    url = 'http://{}'.format(ip)
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find(id="HomeDeviceName")
    if not data:
        data = soup.find("td", {"class": "mastheadTitle"})
        data = data.find("h1")
    return data.contents[0]
