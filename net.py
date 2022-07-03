import socket
import requests
import json
import os, re
import netifaces
from requests.models import Response

# Get private ip
hostname = socket.gethostname()
# Find default gateway ip
gateway = netifaces.gateways() #eth0
iface=gateway['default'][2][1] # Default network interface being used to make outside connections
intip= gateway['default'][2][0] # Internal private ip of the default network card

# get the default network interface mac address
addr=netifaces.ifaddresses(str(gateway))
mac=addr[netifaces.AF_LINK][0]['addr']

url = "http://macvendors.co/api/vendorname/"
# Use get method to fetch details
response = requests.get(url+mac) #attach query to api url
vendor = response.content.decode() #resolve for vendor name
    
# Get public ip
extip=requests.get('https://api.ipify.org').text

#Call an api to get information on the ipv4 address
request_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=64781d95576c4b3fb07b8611579805b2&ip_address=' + extip
response = requests.get(request_url)
result = response.content.decode()
# Convert this data into a dictionary
result  = json.loads(result)
# Organize the data
city=result['city']
region=result['region']
region_code=result['region_iso_code']
country=result['country']
country_code=result['country_code']
continent=result['continent']
longit=result['longitude']
lat=result['latitude']
timezone=result['timezone']['name']
connection_type=result['connection']['connection_type']
isp_name=result['connection']['isp_name']
organization_name=result['connection']['organization_name']

with open('scan.txt','w') as f:
    f.write('Hostname: '+hostname)
    f.write('\nPrivate IP: '+intip)
    f.write('\nPublic IP: '+extip)
    f.write('\nConnection Type: '+connection_type)
    f.write('\nISP Name: '+isp_name)
    f.write('\nOrganization Name: '+organization_name)
    f.write('\n'+'City: '+city)
    f.write('\nRegion: '+region)
    f.write('\nCountry: '+country)
    f.write('\nContinent: '+continent)
    f.write('\nTimezone: '+timezone)
    f.write('\nLatitude: '+str(lat))
    f.write('\nLongitude: '+str(longit))
    f.write('\n')
    f.write('\nInterface Name: '+iface)
    f.write('\nMac Address: '+mac)
    f.write('Vendor: '+vendor)
    
