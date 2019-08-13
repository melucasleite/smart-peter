from bs4 import BeautifulSoup
import requests
import json


def count_printers():
    json_file = open('printers.json')
    printers = json.load(json_file)
    json_file.close()
    for printer in printers:
        ip = printer['ip']
        print ''
        print "Counting {} @ {}".format(printer['ipp'], printer['ip'])
        response = requests.get('http://{}'.format(ip), verify=False)
        response2 = requests.get(
            'http://{}/DevMgmt/ProductUsageDyn.xml'.format(ip), verify=False)
        response3 = requests.get(
            'http://{}/hp/device/InternalPages/Index?id=UsagePage'.format(ip), verify=False)
        f = open('responses/{}.txt'.format(ip), 'w+')
        f2 = open('responses/{}-2.txt'.format(ip), 'w+')
        f3 = open('responses/{}-3.txt'.format(ip), 'w+')
        scrap_home(f.read())
        scrap_xml(f2.read())
        scrap_usage_page(f3.read())
        f.write(response.content)
        f2.write(response2.content)
        f3.write(response3.content)
        f.close()
        f2.close()
        f3.close()


def scrap_home(content):
    soup = BeautifulSoup(content, 'html.parser')
    field = soup.find(id="HomeDeviceName")
    field2 = soup.find("td", {"class": "mastheadTitle"})
    if field2:
        field2 = field2.find("h1")
    if field:
        print "HOME Scrapper: {}".format(field.contents[0])
    if field2:
        print "HOME Scrapper: {}".format(field2.contents[0])


def scrap_xml(content):
    soup = BeautifulSoup(content, 'xml')
    field = soup.find('TotalImpressions')
    if field:
        print "XML Scrapper: {}".format(field.contents[0])

def scrap_usage_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    field = soup.find(id="UsagePage.EquivalentImpressionsTable.Print.Total")
    if field:
        print "Use Page Scrapper: {}".format(field.contents[0])