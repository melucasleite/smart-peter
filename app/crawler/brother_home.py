from bs4 import BeautifulSoup
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def brother_home(ip):
    try:
        url = 'http://{}'.format(ip)
        print url
        response = requests.get(url, verify=False, timeout=(2, 5))
        print response
        content = response.content.lower()
        soup = BeautifulSoup(content, 'html.parser')
        data = soup.findAll("td", {"class": "elemwhite"})
        data = data[4].contents[0]
        counter = filter(lambda x: x.isdigit(), data)
        return counter
    except Exception as e:
        return None
        print str(e)
