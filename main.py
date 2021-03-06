# import required dependencies
import json
import requests
import os
from tabulate import tabulate


def get_ip_info():
    data = []
    # get ip address
    user_ip = requests.get('http://ip.42.pl/raw').text
    # get location information based off of IP address
    url = 'http://ip-api.com/json/' + user_ip
    response = requests.get(url)
    js = response.json()
    data.append({
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
        })
    return data


def get_geo_str(lat, lon):
    return str(lat) + "," + str(lon)
# convert float to string

if __name__ == '__main__':
    data = get_ip_info()
    print(tabulate(data, headers="keys", tablefmt='github'))
