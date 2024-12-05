from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
from selenium.webdriver.common.action_chains import ActionChains

page_slug = 'Theanh28'

def get_post_ids():
    # Set up Chrome WebDriver with WebDriver Manager
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications") 
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Login to Facebook
        driver.get('https://www.facebook.com/')
        script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("sb=8A7xZpRvceNlNa8_L10H6gmO; datr=8A7xZkEKqe6MmLFSnTcYpyte; ps_l=1; ps_n=1; dpr=1.25; locale=vi_VN; c_user=100023060713820; xs=47%3A9W11fUd-wzjQJg%3A2%3A1732613299%3A-1%3A6175; fr=1TWusVqVfBBvdBTZb.AWWwuLIVn1TqETV-ZGvcG2OJss0.BnRWz1..AAA.0.0.BnRZS1.AWXfJ_BMwIE"); location.href = "https://facebook.com"; })();'
        driver.execute_script(script) # Wait for login to complete

        # Navigate to the Facebook page
        # driver.get(f"https://www.facebook.com/{page_slug}/posts/pfbid04p55xgXUvnKR7FP83ERrWXJHUPyvmFf53CtKZMJtsufEz7STKZPud5RpgPiKBb9Dl")
        driver.get('https://www.facebook.com/thealbertadvert/posts/pfbid0jfJ3RMrgtYcHi7gDpR1NGJiXkH8LRyaRp2eNwaQYpX48vWc8mWbVQua79PJhsizbl')
        time.sleep(5)  # Wait for the page to load
        i =1
        try:
            # Xác định phần tử theo XPath
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span/a")
            # Tạo hành động hover
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            time.sleep(1)
            element_2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/span")
            hidden_text = element_2.text  # Hoặc dùng get_attribute nếu text nằm trong một thuộc tính
            print("Nội dung ẩn:", hidden_text)

        except Exception as e:
            print(f"Lỗi: {e}")
        element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/span/div/span/span")
        text = element.text
        print("Số cmt:", text)

        element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/span/div/span/span")
        text = element.text
        print("Số share:", text)

        element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[1]/span/span")
        text = element.text
        print("Số tương tác:", text)


        try:
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[2]/div[2]/div/div/span/div/div/i")
            element.click()
            print("Đã nhấn vào element!")
        except Exception as e:
            print(f"Lỗi: {e}")
        
        try:
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[3]")
            element.click()
            print("Đã nhấn vào element!")
        except Exception as e:
            print(f"Lỗi: {e}")
        time.sleep(2)
        frame = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]')
        j = 1

        while True:
            try:
                print(j)
                element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[2]/div[3]/div[{j}]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/span/a/span/span")
                text = element.text
                print("Tên:", text)
                try:
                    element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[2]/div[3]/div[{j}]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/span/div")
                    text = element.text
                    print("Comment:", text)
                except:
                    pass
                try:
                    image_element = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[2]/div[3]/div[{j}]/div/div[1]/div/div[2]/div[2]/div/div[1]/a/img')

                    # Lấy URL của hình ảnh
                    image_url = image_element.get_attribute("alt")

                    print("Image URL:", image_url)
                except:
                    pass
                j = j+1
            except Exception as e:
                scroll_top = driver.execute_script("return arguments[0].scrollTop;", frame)
                scroll_height = driver.execute_script("return arguments[0].scrollHeight;", frame)
                client_height = driver.execute_script("return arguments[0].clientHeight;", frame)

                # Nếu cuộn đến cuối, thoát vòng lặp
                if scroll_top + client_height >= scroll_height:
                    print("Đã cuộn đến cuối.")
                    break

                # Cuộn thêm một đoạn
                driver.execute_script("arguments[0].scrollBy(0, arguments[0].clientHeight);", frame)
                time.sleep(3)

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    get_post_ids()
