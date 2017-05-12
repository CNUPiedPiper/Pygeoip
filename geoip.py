#-*- coding: utf-8 -*-
import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def Record(target):
    rec = gi.record_by_name(target)
    country = rec['country_name']
    city = rec['city']
    lon = rec['longitude']
    lat = rec['latitude']
    print("Country : ", country)
    print("City : ", city)
    print("lon, lat : ", lon, lat)

if __name__ == "__main__":
    f = open('ip.txt', 'r')
    ip = f.readline()[11:-1]
    f.close()
    Record(ip)
