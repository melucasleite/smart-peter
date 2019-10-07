import requests
import re
import subprocess
import json


def find_printers_lpinfo():
    printers = []
    ipps_string = subprocess.check_output(["lpinfo", "-v"])
    ipps_matches = re.finditer(r"ipp://(.*?.local)", ipps_string, re.MULTILINE)
    ipps = map(lambda match: match.groups()[0], ipps_matches)
    for ipp in ipps:
        ip_string = subprocess.check_output(["ping", ipp, "-w 2", "-c 1"])
        ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", ip_string)[0]
        printer = {
            'ip': ip,
            'ipp': ipp
        }
        printers.append(printer)
    print "Found {} printers.".format(len(printers))
    f = open("printers.json", "w+")
    f.write(json.dumps(printers))
    f.close()
    return printers
