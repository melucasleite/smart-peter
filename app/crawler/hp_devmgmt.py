from bs4 import BeautifulSoup
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def hp_devmgmt(ip):
    url = 'http://{}/DevMgmt/ProductUsageDyn.xml'.format(ip)
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'xml')
    data = soup.find('TotalImpressions')
    return data.contents[0]
