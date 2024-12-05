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

phone_number = '0123456879'
password = 'password'
page_slug = 'thealbertadvert'
def filter_by_month(updated_data, target_month):
    filtered_data = [row for row in updated_data if row[0].split('/')[1] == target_month]
    return filtered_data
def convert_date(date_str):
    # Tách phần ngày tháng trước "lúc"
    date_part = date_str.split(' lúc ')[0]
    # Bỏ "Thứ ..." và "Tháng"
    clean_date = ' '.join(date_part.split(',')[1:]).replace('Tháng ', '').strip()
    # Chuyển đổi chuỗi sang định dạng ngày tháng
    date_object = datetime.strptime(clean_date, '%d %m %Y')
    return date_object.strftime('%d/%m')
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
        driver.get(f'https://www.facebook.com/{page_slug}')
        time.sleep(5)  # Wait for the page to load
        post_id_list = []
        post_video = []
        i = 1
        max_retries = 3
        retry_count = 0
        actions = ActionChains(driver)
        while i<20:
            try:
                # Tìm phần tử thông qua XPath
                element = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[{i}]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span/a')
                
                # Di chuyển chuột đến phần tử
                actions.move_to_element(element).perform()
                element_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div')
                text = element_2.text
                print("Số tương tác:", text)
                # Lấy thuộc tính href
                href = element.get_attribute("href")
                match = re.search(r'pfbid[a-zA-Z0-9]+', href)
                
                if match:
                    result = match.group()  # Lấy kết quả khớp
                    post_id_list.append(result)
                else:
                    print("No match found")
                i += 1
                retry_count = 0

            except Exception as e:
                print(f"Error: {e}")
                
                # Cuộn trang xuống
                driver.execute_script('window.scrollBy(0, window.innerHeight);')
                time.sleep(2)  # Đợi một chút để trang có thể tải thêm nội dung
                
                # Kiểm tra nếu đã cuộn đến cuối trang
                current_scroll_height = driver.execute_script("return document.documentElement.scrollTop + window.innerHeight;")
                total_scroll_height = driver.execute_script("return document.documentElement.scrollHeight;")

                if current_scroll_height == total_scroll_height:  # Nếu đã đến cuối trang
                    print("Reached the bottom of the page.")
                    break  # Dừng vòng lặp
                
                # Nếu trang vẫn còn cuộn nhưng không tìm thấy phần tử, tăng số lần thử
                retry_count += 1
                if retry_count >= max_retries:  # Dừng vòng lặp nếu thử quá nhiều lần mà không tìm được phần tử
                    print("Max retries reached, breaking the loop.")
                    break
        print(len(post_id_list))
        for post_id in post_id_list:
            print(post_id)
            driver.get(f'https://www.facebook.com/{page_slug}/posts/{post_id}')
            # element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/span/div/span/span")
            # text = element.text
            # print("Số cmt:", text)

            # element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/span/div/span/span")
            # text = element.text
            # print("Số share:", text)
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

            element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[1]/span/span")
            text = element.text
            print("Số tương tác:", text)
            post_video.append([hidden_text,int(text)])

        # Cập nhật dữ liệu với định dạng ngày mới
        updated_data = [[convert_date(row[0]), row[1]] for row in post_video]

        # In kết quả
        print(updated_data)

        filtered_data = filter_by_month(updated_data, "11")

        # Tách dữ liệu sau khi lọc thành ngày và giá trị
        dates = [row[0] for row in filtered_data]
        values = [int(row[1]) for row in filtered_data]

        # Vẽ biểu đồ
        plt.figure(figsize=(10, 6))  # Kích thước biểu đồ
        plt.bar(dates, values, color='skyblue', width=0.6)  # Vẽ cột với chiều rộng 0.6

        # Tùy chỉnh biểu đồ
        plt.title('Biểu đồ số lượng tương tác theo ngày (Tháng 11)', fontsize=16)  # Tiêu đề
        plt.xlabel('Thời gian (Tháng 11)', fontsize=12)  # Nhãn trục X
        plt.ylabel('Số tương tác', fontsize=12)  # Nhãn trục Y
        plt.xticks(rotation=45, ha='right', fontsize=10)  # Xoay nhãn trục X
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # Thêm lưới ngang

        # Hiển thị biểu đồ
        plt.tight_layout()  # Điều chỉnh để không bị cắt nội dung
        plt.show()
        # print(post_id_list[0])
        # driver.get(f"https://www.facebook.com/{page_slug}/posts/{post_id_list[1]}")
        # time.sleep(2)

        # j = 3
        # # element_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[3]/div[1]/div/div/div/div/span')
        # # element_2 = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[2]/div[3]/div[{j}]/div/div[1]/div/div[2]/div[1]/div[1]/div/div')
        # element_2 = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[2]/div[3]/div[{j}]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/span/a/span/span')
        

        # # Đọc nội dung text từ element
        # text = element_2.text
        # print("Nội dung text là:", text)

        # time.sleep(1000)
        # seen_links = set()
        # scroll_count = 30  # Number of scrolls to perform

        # for _ in range(scroll_count):
        #     # Scroll down to the bottom of the page
        #     driver.execute_script('window.scrollBy(0, window.innerHeight);')
        #     time.sleep(2)  # Wait for new posts to load

        #     # Find all elements matching the XPath
        #     new_links = driver.find_elements(By.XPATH,
        #     '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span/a'
        #     )
        #     # Extract and store unique hrefs
        #     for link in new_links:
        #         # driver.execute_script('arguments[0].scrollIntoView();', link)
        #         # actions = ActionChains(driver)
        #         # actions.move_to_element(link).perform()
        #         # time.sleep(2)
        #         href = link.get_attribute("href")
        #         if href and href not in seen_links:
        #             seen_links.add(link)
        # driver.execute_script('window.scrollTo(0, 0);')
        # print(f"Total unique links found: {len(seen_links)}")
        # print("Links:")
        # driver.execute_script(
        # """
        # document.querySelectorAll('[role="banner"], [style*="z-index"]').forEach(function(el) {
        #     el.style.display = 'none';
        # });
        # """
        # )
        # # time.sleep(1000)
        # actions = ActionChains(driver)
        # for link in seen_links:
        #     driver.execute_script('arguments[0].scrollIntoView();', link)
        #     actions.move_to_element(link).perform()
        #     href = link.get_attribute('href')
        #     print("Href:", href)
        #     time.sleep(1)

        # for _ in range(5):  # Adjust the range for more posts
        #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #     time.sleep(2)  # Wait for new posts to load

        # all_links = driver.find_elements(By.XPATH,
        #     '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/a'
        # )
        # print(len(all_links))
        # element_list = []
        # for _ in range(5):  # Adjust the range for more posts
        #     elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span/a')
        #     for element in elements:
        #         element_list.append(element)
        #     print(len(elements))
        #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #     time.sleep(5)
        # print(len(element_list))
        # element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span/a')
        # print("Element found!")

        # # Hide banners
        # driver.execute_script(
        #     """
        #     document.querySelectorAll('[role="banner"], [style*="z-index"]').forEach(function(el) {
        #         el.style.display = 'none';
        #     });
        #     """
        # )
        # time.sleep(10)
        # actions = ActionChains(driver)
        # for element in elements[:len(elements)-2]:
        #     driver.execute_script('arguments[0].scrollIntoView();', element)
        #     time.sleep(1)
        #     actions.move_to_element(element).perform()
        #     href = element.get_attribute('href')
        #     print("Href:", href)
        #     time.sleep(1)
        # time.sleep(10)


        # for _ in range(1):  # Adjust the range for more posts
        #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #     time.sleep(5)
        # elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span/a')
        # print(len(elements))

        # time.sleep(10)
        # actions = ActionChains(driver)
        # for element in elements[:len(elements)-2]:
        #     driver.execute_script('arguments[0].scrollIntoView();', element)
        #     time.sleep(1)
        #     actions.move_to_element(element).perform()
        #     href = element.get_attribute('href')
        #     print("Href:", href)
        #     time.sleep(1)
        # time.sleep(10)

        # if element.is_displayed():  # Check if the element is visible
        #     driver.execute_script("arguments[0].scrollIntoView(true);", element)
        #     print("Scrolled into view!")
        # else:
        #     print("Element is not visible or does not exist.")

        # time.sleep(100)
        # element = driver.find_element(By.XPATH, )

        # driver.execute_script('arguments[0].scrollIntoView();', element)
        # actions = ActionChains(driver)
        # # Print the count of elements
        # for i in range(1,5):
        #     element = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[{i}]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span/a')
        #     driver.execute_script('arguments[0].scrollIntoView();', element)
        #     time.sleep(1)
        #     actions.move_to_element(element).perform()
        #     href = element.get_attribute('href')
        #     print("Href:", href)
        #     time.sleep(1)
        # Scroll down to load posts
        # for _ in range(5):  # Adjust the range for more posts
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(2)  # Wait for new posts to load

        # Find all links
# Tìm các phần tử với XPath
        # element = driver.find_element(By.XPATH,
        #     '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span/a'
        # )

        # # Hover vào phần tử
        # actions = ActionChains(driver)
        # actions.move_to_element(element).perform()
        # href = element.get_attribute('href')
        # print("Href:", href)
        # # In ra thông báo xác nhận
        # print("Hovered successfully over the element.")
        # time.sleep(1000)


    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    get_post_ids()
