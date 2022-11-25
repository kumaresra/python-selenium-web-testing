from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

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
driver.quit()
  