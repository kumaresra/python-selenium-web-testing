import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import requests
import time
from common.settings import *

from common.colors import bcolors

driver = None
service = None

def init_service():
  service = ChromeService(executable_path=ChromeDriverManager().install())


def get_driver():
  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  driver = webdriver.Chrome(options=options)
  return driver

def printBanner():
    print(bcolors.OKGREEN + """

 ██████   █████  ███    ███ ███████ ██████   █████  ██    ██ 
██       ██   ██ ████  ████ ██      ██   ██ ██   ██  ██  ██  
██   ███ ███████ ██ ████ ██ █████   ██████  ███████   ████   
██    ██ ██   ██ ██  ██  ██ ██      ██      ██   ██    ██    
 ██████  ██   ██ ██      ██ ███████ ██      ██   ██    ██    
                                                             
                                                                                                                              
                                                                                                                                                                  
    """ + bcolors.ENDC)

def title_check(url,given_title):
  print(bcolors.OKBLUE + 'Check title for Website: +'f' {url}' + bcolors.ENDC)
  driver = get_driver()
  driver.get(url)
  title = driver.title

  try:
    assert title == given_title
    print(bcolors.OKGREEN + 'Success: Title match for Site: 'f' {url}' + bcolors.ENDC)
  except:
    print(bcolors.FAIL + 'Title match Failed: +'f' {url}' + bcolors.ENDC)
  driver.implicitly_wait(5)

def scroll_page_to_bottom(driver):
  time.sleep(5)
  height = int(driver.execute_script("return document.documentElement.scrollHeight"))
  while True:
    driver.execute_script('window.scrollBy(0,10)')
    time.sleep(0.10)
    totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
    if totalScrolledHeight >= height:
        driver.switch_to.window(driver.window_handles[0])
        break
  print('***Web Page Visited***')


def login_with_test_id(web_url,username,passwd):
  print(bcolors.OKBLUE + 'Logging with Test ID: +'f' {username}' + bcolors.ENDC)
  driver = get_driver()
  driver.get(web_url)
  el = driver.find_element(By.CSS_SELECTOR, ".call-to-action:nth-child(3) > .fill-btn")
  assert el.text == "LOGIN"
  driver.find_element(By.CSS_SELECTOR, ".call-to-action:nth-child(3) > .fill-btn").click()
  driver.implicitly_wait(1000)
  e2 = driver.find_element(By.XPATH, "//button/span[2]")
  assert e2.text == "Login With Email"

  driver.find_element(By.XPATH, "//button/span[2]").click()
  driver.implicitly_wait(1000)

  #css=div:nth-child(2) > input
  e3 = driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input")
  #assert el.text == "LOGIN With Email"
  driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input").send_keys(username)

  driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > input").send_keys(passwd)

  driver.find_element(By.CSS_SELECTOR, ".call-to-action:nth-child(4) > .fill-btn").click()
  driver.implicitly_wait(10000)
  try:
      user = driver.find_element(By.CSS_SELECTOR,"#_menustyle_header__DI6Np > div._menustyle_menu_group__P1YTs > div:nth-child(2) > div > div._menustyle_userprofile__TkNC2 > div > div._menustyle_user_name__o9IMK").text
      print ("Username: "+ user)
      assert user == "Rahulrastogi61"
      print(bcolors.OKGREEN + 'Login Success: 'f' {username}'  + bcolors.ENDC)
  except: 
      print(bcolors.FAIL + 'Failed to login with USER: 'f' {username}'  + bcolors.ENDC)
  


def check_all_hyperlinks(url):
  print(bcolors.OKBLUE + 'Checking URL: +'f' {url}' + bcolors.ENDC)
  driver = get_driver()
  driver.get(url)
  scroll_page_to_bottom(driver=driver)
  # fetch all the anchor tags from this page
  elems = driver.find_elements(By.TAG_NAME,"a")
  #check each link if it is broken or not
  for link in elems:
      try:
        url = link.get_attribute('href')
        if not url.startswith("mailto:"):
          result = requests.head(url)
        #if status code is not 200 then print the url (customize the if condition according to the need)
        if result.status_code != 200:
          print(bcolors.FAIL + 'Failed: 'f' {url}' +'| Status code: '+ f'{result.status_code}' + bcolors.ENDC)
        else:
          print(bcolors.OKGREEN + 'Success: +'f' {url}' + bcolors.ENDC)
      except:
        print("Link not reachable " + str(link.title))


if __name__ == '__main__':
  load_env()
  init_service()
  printBanner()
  title_check("https://gamepay.sg","Gamepay - Play To Earn NFT - Exclusive NFT Marketplace")
  login_with_test_id("https://gamepay.sg",getTestUsername(),getTestPassword())
  check_all_hyperlinks("https://gamepay.sg")
