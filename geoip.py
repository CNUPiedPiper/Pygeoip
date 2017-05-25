#-*- coding: utf-8 -*-
import pygeoip
import requests
from bs4 import BeautifulSoup

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def Record(target):
    rec = gi.record_by_name(target)
    country = rec['country_name']
    city = rec['city']
    lat = rec['latitude']
    lon = rec['longitude']
    print(city, lat, lon)
    return city, lat, lon

if __name__ == "__main__":
    r = requests.get('http://ip.ojj.kr')
    soup = BeautifulSoup(r.text, 'html.parser')
    result = soup.find('font',attrs={'face':'verdana', 'color':'RED'})
    ip = result.text
    Record(ip)
