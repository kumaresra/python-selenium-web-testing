from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import requests
import time

service = ChromeService(executable_path=ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("https://gamepay.sg")

title = driver.title

try:
  assert title == "Gamepay - Play To Earn NFT - Exclusive NFT Marketplace" , "title is valid"
  print("title is valid")
except:
  print("Title is not matching...")

driver.implicitly_wait(5)

el = driver.find_element(By.CSS_SELECTOR, ".call-to-action:nth-child(3) > .fill-btn")
assert el.text == "LOGIN"

driver.find_element(By.CSS_SELECTOR, ".call-to-action:nth-child(3) > .fill-btn").click()

driver.implicitly_wait(1000)

#driver.switch_to.window()

e2 = driver.find_element(By.XPATH, "//button/span[2]")
assert e2.text == "Login With Email"


driver.find_element(By.XPATH, "//button/span[2]").click()

driver.implicitly_wait(1000)

#css=div:nth-child(2) > input
e3 = driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input")
#assert el.text == "LOGIN With Email"
driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input").send_keys("rahulrastogi61@gmail.com")

driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > input").send_keys("Aaravananya9$")

#el = driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/div[2]/div/div[1]/div/div[3]/button/span[2]")
# assert el.text == "login with Email"
#.call-to-action:nth-child(4) > .fill-btn

driver.find_element(By.CSS_SELECTOR, ".call-to-action:nth-child(4) > .fill-btn").click()
driver.implicitly_wait(10000)
try:
    assert driver.find_element(By.XPATH,"//*[@id=\"_menustyle_header__DI6Np\"]/div[2]/div[2]/div/div[3]/div/div[2]").text == "Rahulrastogi61"
    print("User  loggedin")
except: 
    print("User not loggedin")

    #.rounded-circle:nth-child(1) > a
    #get all links
# all_links = driver.find_elements(By.CSS_SELECTOR,"a")
# print("the list")
# print(all_links)
driver.get("https://gamepay.sg")
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



elems = driver.find_elements(By.TAG_NAME,"a")
print(len(elems))
for elem in elems:
  try:
    print(elem.get_attribute("href"))
  except:
    print("exception at: " + str(elem.text))

#check each link if it is broken or not
for link in elems:
    #extract url from href attribute
    if link.get_attribute('href') is not None:
      url = link.get_attribute('href')
    #print("printing")
    #print(link)
      #send request to the url and get the result
      result = requests.head(url)
      print(url.title)
      #if status code is not 200 then print the url (customize the if condition according to the need)
      if result.status_code != 200:
        print(url, result.status_code)

driver.quit()