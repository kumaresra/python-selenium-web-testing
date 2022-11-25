import datetime
import os
import random
import time

import pandas as pd
import psutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from common.colors import bcolors
from common.download_driver import download_driver
from common.load_files import get_hash, load_search, load_url
from common.proxies import load_proxy


def printBanner():
    print(bcolors.OKGREEN + """
 __          __         _         _______                   __    __   _        
 \ \        / /        | |       |__   __|                 / _|  / _| (_)       
  \ \  /\  / /    ___  | |__        | |     _ __    __ _  | |_  | |_   _    ___ 
   \ \/  \/ /    / _ \ | '_ \       | |    | '__|  / _` | |  _| |  _| | |  / __|
    \  /\  /    |  __/ | |_) |      | |    | |    | (_| | | |   | |   | | | (__ 
     \/  \/      \___| |_.__/       |_|    |_|     \__,_| |_|   |_|   |_|  \___|
                                                                                
                                                                                
                                                                                                                                                                  
    """ + bcolors.ENDC)

proxy = None
status = None
start_time = None
cancel_all = False

urls = []
queries = []
suggested = []

hash_urls = None
hash_queries = None
hash_config = None
bad_proxies = []

min_threads=1
max_threads=5


def detect_file_change():
    global hash_urls, hash_queries, urls, queries

    if hash_urls != get_hash("urls.txt"):
        hash_urls = get_hash("urls.txt")
        urls = load_url()
        suggested.clear()

    if hash_queries != get_hash("search.txt"):
        hash_queries = get_hash("search.txt")
        queries = load_search()
        suggested.clear()

def main_viewer(proxy_type, proxy, position):
    global width, viewports
    driver = None
    data_dir = None

    if cancel_all:
        raise KeyboardInterrupt


def load_input_files():
    urls = load_url()
    queries = load_search()
    hash_urls = get_hash("urls.txt")
    hash_queries = get_hash("search.txt")
    print(bcolors.OKBLUE + 'Hash for url:'+ f'{hash_urls}' +'| parsed urls ' + bcolors.ENDC)
    print(bcolors.OKBLUE + 'Hash for Queries: +'f' {hash_queries}' + '| parsed urls ' + bcolors.ENDC)

def get_proxy_list(filename):
    proxy_list = load_proxy(filename)
    return proxy_list




def main():
    #load driver
    # cwd = os.getcwd()
    # patched_drivers = os.path.join(cwd, 'patched_drivers')
    # osname, exe_name = download_driver(patched_drivers=patched_drivers)
    # proxy_filename = 'proxies.txt'
    # proxy_list = get_proxy_list(proxy_filename)
    # print(bcolors.OKCYAN +
    #           f'Total proxies : {len(proxy_list)}' + bcolors.ENDC)

    # proxy_list = [x for x in proxy_list if x not in bad_proxies]
    # if len(proxy_list) == 0:
    #     bad_proxies.clear()
    #     proxy_list = get_proxy_list()
    # if proxy_list[0] != 'dummy':
    #     proxy_list.insert(0, 'dummy')
    # if proxy_list[-1] != 'dummy':
    #     proxy_list.append('dummy')
    # total_proxies = len(proxy_list)


    # threads = random.randint(min_threads, max_threads)

    # loop = 0
    # pool_number = list(range(total_proxies))
    # print('pool_number: '+ str(pool_number))



    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    col_name = ['url']
    df_url = pd.read_csv("urls.txt", names=col_name)

    # while True:
    website_random_URL = random.sample(df_url.url.to_list(), 1)

    driver.get(website_random_URL[0])
    time.sleep(5)
    height = int(driver.execute_script("return document.documentElement.scrollHeight"))
    print('Hitting Url : '+ website_random_URL[0])
    while True:
        driver.execute_script('window.scrollBy(0,10)')
        time.sleep(0.10)
        totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
        if totalScrolledHeight >= height:
            driver.switch_to.window(driver.window_handles[0])
            break
    print('***Web Page Visited***')


if __name__ == '__main__':
    printBanner()
    # load_input_files()
    main()
 