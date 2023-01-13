# certified $udo classic

import requests

def bypass(url):
    data = {
        "url": url
    }

    return requests.post("https://api.bypass.vip/", data=data).json()["destination"]

url = input("Enter Linkvertise URL: ")
print(bypass(url))
