from bs4 import BeautifulSoup
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def hp_usagepage(ip):
    url = 'http://{}/hp/device/InternalPages/Index?id=UsagePage'.format(ip)
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find(id="UsagePage.EquivalentImpressionsTable.Print.Total")
    return data.contents[0]
