
from concurrent.futures import ThreadPoolExecutor, wait
from random import randint
from time import gmtime, sleep, strftime, time

import requests
from fake_headers import Headers, browsers
from requests.exceptions import RequestException


def update_chrome_version():
    link = 'https://gist.githubusercontent.com/MShawon/29e185038f22e6ac5eac822a1e422e9d/raw/versions.txt'

    output = requests.get(link, timeout=60).text
    chrome_versions = output.split('\n')

    browsers.chrome_ver = chrome_versions



def spoof_geolocation(proxy_type, proxy, driver):
    try:
        proxy_dict = {
            "http": f"{proxy_type}://{proxy}",
                    "https": f"{proxy_type}://{proxy}",
        }
        resp = requests.get(
            "http://ip-api.com/json", proxies=proxy_dict, timeout=30)

        if resp.status_code == 200:
            location = resp.json()
            params = {
                "latitude": location['lat'],
                "longitude": location['lon'],
                "accuracy": randint(20, 100)
            }
            driver.execute_cdp_cmd(
                "Emulation.setGeolocationOverride", params)

    except (RequestException, Exception):
        pass