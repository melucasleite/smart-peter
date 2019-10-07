from bs4 import BeautifulSoup
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def brother_home(ip):
    url = 'http://{}/general/information.html?kind=item'.format(ip)
    response = requests.get(url, verify=False)
    content = response.content.lower()
    # soup = BeautifulSoup(content, 'html.parser')
    # data = soup.findAll("td", {"class": "elemwhite"})
    # data = data[4].contents[0]
    # counter = filter(lambda x: x.isdigit(), data)
    print "Crawler not implemented."
    return content
