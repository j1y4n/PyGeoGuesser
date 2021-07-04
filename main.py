import json
import requests
import os
from tabulate import tabulate


def get_ip_info():
    user_ip = requests.get('http://ip.42.pl/raw').text
    # get location information based off of IP address
    url = 'http://ip-api.com/json/' + user_ip
    response = requests.get(url)
    js = response.json()
    return {
        'ip': user_ip,
        'success': js['status'] == 'success',
        'city': js['city'],
        'state': js['regionName'],
        'countryCode': js['countryCode'],
        'ip_coords': get_geo_str(js['lat'], js['lon']),
        'country': js['country'],
        'isp': js['isp'],
        'org': js['org'],
        'as': js['as']
    }


def get_geo_str(lat, lon):
    return str(lat) + "," + str(lon)


if __name__ == '__main__':
    city = get_ip_info()['city']
    ip = get_ip_info()['ip']
    coords = get_ip_info()['ip_coords']
    state = get_ip_info()['state']
    country = get_ip_info()['country']
    countryCode = get_ip_info()['countryCode']
    isp = get_ip_info()['isp']
    org = get_ip_info()['org']
    asp = get_ip_info()['as']

    data = [['IP', ip], ['Country', country], ['State', state], ['City', city],
            ['Country Code', countryCode], ['ISP', isp], ['Org', org],
            ['AS', asp], ['COORDS', coords]]
    print(tabulate(data))
