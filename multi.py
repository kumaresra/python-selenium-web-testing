import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email = 'hello@gamepay.sg\n'    #enter mail
password = 'H@game//pay\n'         #enter pass

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)
time.sleep(2)

#upto the above the codes credits goes to https://github.com/xtekky these man

with open("urls.txt") as f: #change url in text file
    for url in f:
        driver.get(url)
        
time.sleep(5) #if video dont have ads then change 8 to 3 or 4       
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()       
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/div[1]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
driver.close()

email = 'hello@gamepay.sg\n'    #enter mail
password = 'H@game//pay\n'         #enter pass

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)
time.sleep(2)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  
        
time.sleep(5) #if video dont have ads then change 8 to 3 or 4         
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/div[1]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
driver.close()


#i here added only two time auto like and sub if you want more means copy line from 32 to 53 and paste in 55th line and dont forgot to remove mail and password do these tricks if want more....

#if you only want like and dont want auto subscribers means remove the 29 and 52 line which contain subscribe xpath code same..
