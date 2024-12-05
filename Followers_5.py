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



def find_element_with_xpaths(driver, xpaths):
    for xpath in xpaths:
        try:
            element = driver.find_element(By.XPATH, xpath)
            return element
        except:
            continue
    return None

chrome_options = Options()
chrome_options.add_argument("--disable-notifications") 
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
page_slug = 'incardnamecardthongminh'

# Login to Facebook
driver.get('https://www.facebook.com/')
script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("sb=8A7xZpRvceNlNa8_L10H6gmO; datr=8A7xZkEKqe6MmLFSnTcYpyte; ps_l=1; ps_n=1; dpr=1.25; locale=vi_VN; c_user=100023060713820; xs=47%3A9W11fUd-wzjQJg%3A2%3A1732613299%3A-1%3A6175; fr=1TWusVqVfBBvdBTZb.AWWwuLIVn1TqETV-ZGvcG2OJss0.BnRWz1..AAA.0.0.BnRZS1.AWXfJ_BMwIE"); location.href = "https://facebook.com"; })();'
driver.execute_script(script) # Wait for login to complete

# Navigate to the Facebook page
driver.get(f'https://www.facebook.com/{page_slug}')
time.sleep(5)
actions = ActionChains(driver)
i = 1
max_retries = 3
retry_count = 0
while i < 10:
    xpaths = [
        f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[{i}]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span/a',
        f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[{i}]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span/a',
        f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[{i}]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[1]/div/a'
    ]
    
    element = find_element_with_xpaths(driver, xpaths)
    if element:
        actions.move_to_element(element).perform()
        href = element.get_attribute("href")
        print("Found:", href)
        i += 1
        retry_count = 0
    else:
        driver.execute_script('window.scrollBy(0, window.innerHeight);')
        time.sleep(2)
        # current_scroll_height = driver.execute_script("return document.documentElement.scrollTop + window.innerHeight;")
        # total_scroll_height = driver.execute_script("return document.documentElement.scrollHeight;")

        # if current_scroll_height == total_scroll_height:  # Nếu đã đến cuối trang
        #     print("Reached the bottom of the page.")
        #     break  

        # # Nếu trang vẫn còn cuộn nhưng không tìm thấy phần tử, tăng số lần thử
        # retry_count += 1
        # if retry_count >= max_retries:  # Dừng vòng lặp nếu thử quá nhiều lần mà không tìm được phần tử
        #     print("Max retries reached, breaking the loop.")
        #     break

