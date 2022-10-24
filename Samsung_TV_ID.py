import socket
import requests
import time

ip = input("Device IP: ")
print("----------------------")

vuln_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = vuln_test.connect_ex((ip, 8001))

if result == 0:
 port = 8001
 url = "http://" + ip + ":" + str(port) + "/api/v2/"
 r = requests.get(url)
 print("Vulnerable!")
 print("----------------------")
 print(r.text)
else:
 print("Not vulnerable or not a vcom-tunnel port, choose manually:")
 print("----------------------")
 input = input("Port: ")
 port = input
 print("----------------------")
 url = "http://" + ip + ":" + str(port) + "/api/v2/"
 r = requests.get(url)
 print(r.text)
 print("----------------------")


