from bs4 import BeautifulSoup
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def count_printers():
    json_file = open('printers.json')
    printers = json.load(json_file)
    json_file.close()
    for printer in printers:
        ip = printer['ip']
        print ''
        print "{} @ {}".format(printer['ipp'].split('.')[0], printer['ip'])
        response = requests.get('http://{}'.format(ip), verify=False)
        response2 = requests.get(
            'http://{}/DevMgmt/ProductUsageDyn.xml'.format(ip), verify=False)
        response3 = requests.get(
            'http://{}/hp/device/InternalPages/Index?id=UsagePage'.format(ip), verify=False)
        response4 = requests.get(
            'http://{}/SSI/info_configuration.htm'.format(ip), verify=False)
        response5 = requests.get(
            'http://{}/DevMgmt/ProductConfigDyn.xml'.format(ip), verify=False)
        f = open('responses/{}.txt'.format(ip), 'w+')
        f2 = open('responses/{}-2.txt'.format(ip), 'w+')
        f3 = open('responses/{}-3.txt'.format(ip), 'w+')
        f4 = open('responses/{}-4.txt'.format(ip), 'w+')
        f5 = open('responses/{}-5.txt'.format(ip), 'w+')
        f.write(response.content)
        f2.write(response2.content)
        f3.write(response3.content)
        f4.write(response4.content)
        f5.write(response5.content)
        f.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        equipment = scrap_home(response.content)
        count_xml = scrap_xml(response2.content)
        count_user_page = scrap_usage_page(response3.content)
        count_config_page = scrap_config_page(response4.content)
        equipment_xml = scrap_equipment_xml(response5.content)
        count_brother_home = scrap_brother_home(response.content)
        if (count_brother_home):
            equipment = scrap_equipment_brother_home(response.content)
        printer['equipment'] = None
        printer['count'] = None
        if equipment:
            printer['equipment'] = equipment
        if count_xml:
            printer['count'] = count_xml
        if equipment_xml:
            printer['equipment'] = equipment_xml
        if count_brother_home:
            printer['count'] = count_brother_home
        if count_user_page:
            printer['count'] = count_user_page
        if count_config_page:
            printer['count'] = count_config_page
    json_file = open('printers.json','w+')
    json_file.write(json.dumps(printers))
    json_file.close()
    return printers


def scrap_home(content):
    soup = BeautifulSoup(content, 'html.parser')
    field = soup.find(id="HomeDeviceName")
    field2 = soup.find("td", {"class": "mastheadTitle"})
    if field2:
        field2 = field2.find("h1")
    if field:
        print "{}".format(field.contents[0])
        return field.contents[0]
    if field2:
        print "{}".format(field2.contents[0])
        return field2.contents[0]
    return None


def scrap_xml(content):
    soup = BeautifulSoup(content, 'xml')
    field = soup.find('TotalImpressions')
    if field:
        print "Page Count: {}".format(field.contents[0])
        return format(field.contents[0])
    return None


def scrap_usage_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    field = soup.find(id="UsagePage.EquivalentImpressionsTable.Print.Total")
    if field:
        print "Page Count: {}".format(field.contents[0])
        return format(field.contents[0])
    return None


def scrap_config_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    field = soup.findAll('table')
    if len(field) < 5:
        return None
    if field:
        field = field[5].find("td", {"class": "itemFont"})
    if field:
        print "Page Count: {}".format(field.contents[0])
        return format(field.contents[0])
    return None


def scrap_equipment_xml(content):
    soup = BeautifulSoup(content, 'xml')
    field = soup.find('dd:MakeAndModelBase')
    if field:
        if not len(field.contents):
            return None
        print field.contents
        print "{}".format(field.contents[0])
        return format(field.contents[0])
    return None

def scrap_equipment_brother_home(content):
    soup = BeautifulSoup(content, 'html.parser')
    field = soup.find("title")
    if field:
        equipment = field.contents[0].strip()
        print equipment
        return equipment
    return None


def scrap_brother_home(content):
    content = content.lower()
    soup = BeautifulSoup(content, 'html.parser')
    field = soup.findAll("td", {"class": "elemwhite"})
    if field:
        field = field[4].contents[0]
        counter = filter(lambda x: x.isdigit(), field)
        print "Page Count: {}".format(counter)
        return format(counter)
    return None