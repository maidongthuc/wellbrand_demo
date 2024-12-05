from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
import csv

import matplotlib.pyplot as plt
from datetime import datetime



def find_element_with_xpaths(driver, xpath):

    try:
        element = driver.find_element(By.XPATH, xpath)
        return element
    except:
        return None

chrome_options = Options()
chrome_options.add_argument("--disable-notifications") 
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
page_slug = 'incardnamecardthongminh'

# Login to Facebook
driver.get('https://www.facebook.com/')
script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("sb=8A7xZpRvceNlNa8_L10H6gmO; ps_l=1; ps_n=1; dpr=1.25; c_user=100023060713820; datr=2jtJZ7gitdvWqxYGwh7rwCOj; xs=27%3AdyTwtWZ25U4mDA%3A2%3A1732852699%3A-1%3A6175; fr=12ZZDyeSoseNmEJEP.AWVtUNlZ8NjySbpmmt029gtsjM0.BnR-lu..AAA.0.0.BnSTvd.AWVCaf_aWcw;"); location.href = "https://facebook.com"; })();'
driver.execute_script(script) # Wait for login to complete

# Navigate to the Facebook page
driver.get(f'https://www.facebook.com/{page_slug}')
time.sleep(10)
actions = ActionChains(driver)

element = find_element_with_xpaths(driver, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[6]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[1]/div/div/a')
if element:
    print('Tìm thấy 1')
else:
    print('không thấy 1')

element = find_element_with_xpaths(driver, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[6]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[1]/div/div')
if element:
    actions.move_to_element(element).perform()
    time.sleep(1)
    element_2 = find_element_with_xpaths(driver, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[6]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[1]/div/div/a')
    if element_2:
        print('Tìm thấy 2')
    else:
        print('không tim thấy 2')
else:
    print('không thấy 3')
