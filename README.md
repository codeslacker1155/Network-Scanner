# Network-Scanner
This is a python script used to scan your network and get back various important information. 

Uses ipify.org api to get public ip of your device, and abstract api for geolocation. The script uses the requests module to make the request to the external resources and returns it as json data. The data is then parsed, organized, and written to a file. The scanner also uses the arpscan -a option to scan the local network. NOTE: The filter is for a Standard Class C address (192.168.68.x). This returns the local address on the network of every device along with its mac address. To know what kind of device it was on the network; vendor verification was added at the end with macvendors.com api being used. 

## What problem does this solve?
You know what devices are on your network and where your external ip is located. This is where any attacker generally would think you are. This can be used to learn your internal ip and your external one as well. This provides useful information on the status of your network in the form of a file created called 'ipscan.txt'.

## What did I learn from building this?
* The different layers to networks
* Different address types
* Regex, filehandling, json


## Why did I build this?
To know what my network is doing not only on the local area network connection but the wireless area network connection as well. This tool is something that I really built for personal use to know when exactly my vpn is working and checking devices on the network.

## Features:
* ipify.org api
* apstract api (geolocation)
* macvendors.com api

## Output File (Example)
<img width="696" alt="Screen Shot 2021-08-03 at 4 36 03 PM" src="https://user-images.githubusercontent.com/47655454/128083149-186a71ae-2c61-49ad-a93d-f1d4a0dc889c.png">
