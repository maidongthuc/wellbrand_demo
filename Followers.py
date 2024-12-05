from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import re
import json
import csv
# Khởi tạo trình duyệt Chrome mà không cần chỉ định path
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")  # Tắt thông báo

# Khởi động trình duyệt với cấu hình
driver = webdriver.Chrome(options=chrome_options)

# Mở trang web
driver.get("https://www.facebook.com/")


script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("sb=8A7xZpRvceNlNa8_L10H6gmO; datr=8A7xZkEKqe6MmLFSnTcYpyte; ps_l=1; ps_n=1; dpr=1.25; locale=vi_VN; c_user=100023060713820; xs=6%3A46k-e0TONisNUg%3A2%3A1732434499%3A-1%3A6175%3A%3AAcX8aGpIXQ8ZpO2wCP6NIe-ET6vSOyTtlLxGW3IE0jU; fr=1Y2TxHW74tma0B0ll.AWXdAZTO-jIhl0b4t6bWL9JHZrM.BnRArq..AAA.0.0.BnRA1W.AWWPaqtp5Zw"); location.href = "https://facebook.com"; })();'
driver.execute_script(script)
driver.get("https://www.facebook.com/Theanh28") #Bỏ link ở đây
sleep(2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
# sleep(5)
share_buttons = driver.find_elements(By.XPATH, '//div[contains(text(), "Chia sẻ")]')
print(share_buttons)
print(f"Số lượng nút 'Chia sẻ' tìm thấy: {len(share_buttons)}")
sleep(100)

# sleep(5)
# def read_data(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             return file.read().splitlines()
#     except FileNotFoundError:
#         return []
# def write_file(file_path, data):
#     try:
#         with open(file_path, 'a') as file:
#             file.write(data + '\n')
#     except Exception as e:
#         print("Lỗi khi ghi file:", str(e))
# def get_post_ids(driver, file_path='posts.csv'):
#     try:
#         all_posts = set(read_data(file_path))  # Đọc danh sách ID bài viết đã lưu
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # Cuộn xuống cuối trang
#         sleep(2)
#         share_buttons = driver.find_elements(By.XPATH, '//a[contains(@href, "/sharer.php")]')
#         for link in share_buttons:
#             post_id = re.search(r"sid=(\d+)", link.get_attribute('href'))
#             if post_id and post_id.group(1) not in all_posts:
#                 print("Tìm thấy Post ID:", post_id.group(1))
#                 write_file(file_path, post_id.group(1))
#     except Exception as e:
#         print("Lỗi khi lấy Post ID:", str(e))
# file_path="D:/TAA/post.csv"
# while len(read_data(file_path)) < 10:
#     get_post_ids(driver, file_path)
# # Tìm phần tử bằng XPath
# xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[2]/div/div[2]/div/div[2]/span/div/span[1]/span/span"
# element = driver.find_element(By.XPATH, xpath)

# # Lấy thông tin
# print("Nội dung:", element.text)
# print("Thuộc tính href:", element.get_attribute("href"))

# try:
#     # Sử dụng XPath để tìm thẻ <a> chứa Post ID
#     post_element = driver.find_element(By.XPATH, '//a[contains(@href, "pfbid")]')
#     href_value = post_element.get_attribute("href")  # Lấy giá trị thuộc tính href
#     print("Href value:", href_value)

#     # Trích xuất Post ID từ href bằng regex
#     match = re.search(r"pfbid\w+", href_value)  # Tìm chuỗi bắt đầu bằng `pfbid` theo sau là các ký tự
#     if match:
#         post_id = match.group(0)  # Lấy giá trị Post ID
#         print("Post ID:", post_id)
#     else:
#         print("Không tìm thấy Post ID trong href!")
# except Exception as e:
#     print("Có lỗi xảy ra:", e)

# try:
#     element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/h1')
#     content = element.text  # Lấy nội dung văn bản của phần tử
#     print("Tên của Page", content)
# except Exception as e:
#     print("Không tìm thấy phần tử hoặc lỗi:", str(e))
# try:
#     follower_element = driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]')
#     followers_text = follower_element.text  # Lấy toàn bộ nội dung văn bản của phần tử
#     followers_count = int(followers_text.split()[0])  # Tách số lượng người theo dõi (200)
#     print(f"Số lượng người theo dõi: {followers_count}")
# except Exception as e:
#     print("Không thể tìm thấy số lượng người theo dõi:", e)

# try:
#     like_element = driver.find_element(By.XPATH, '//a[contains(@href, "/friends_likes/")]')
#     likes_text = like_element.text  # Lấy toàn bộ nội dung văn bản của phần tử
#     likes_count = int(likes_text.split()[0])  # Tách số lượt thích (577)
#     print(f"Số lượt thích: {likes_count}")
# except Exception as e:
#     print("Không thể tìm thấy số lượt thích:", e)
	
	

# try:
#     element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div[1]')
#     element.click()  # Nhấn vào phần tử
#     # print("Đã nhấn vào phần tử thành công!")
# except Exception as e:
#     print("Không tìm thấy phần tử hoặc lỗi:", str(e))
# sleep(1)
# try:
#     element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[3]/a')
#     element.click()  # Nhấn vào phần tử
#     # print("Đã nhấn vào phần tử thành công!")
# except Exception as e:
#     print("Không tìm thấy phần tử hoặc lỗi xảy ra:", str(e))
# sleep(2)
# try:
#     element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/span')
#     content = element.text  # Lấy nội dung văn bản của phần tử
#     print("ID Page:", content)
# except Exception as e:
#     print("Không tìm thấy phần tử hoặc lỗi:", str(e))
sleep(1)
# try:
#     element = driver.find_element(By.XPATH, "//a[contains(@href, 'pfbid')]")  # Tìm thẻ <a> chứa `pfbid` trong href
#     href_value = element.get_attribute("href")  # Lấy giá trị thuộc tính href
#     print("Giá trị href:", href_value)
    
#     # Trích xuất giá trị `pfbid` từ URL bằng regex
#     match = re.search(r"pfbid\w+", href_value)  # Tìm chuỗi bắt đầu bằng `pfbid` theo sau là các ký tự
#     if match:
#         pfbid = match.group(0)
#         print("Giá trị pfbid:", pfbid)
#     else:
#         print("Không tìm thấy giá trị pfbid trong URL!")
# except Exception as e:
#     print("Không tìm thấy phần tử hoặc xảy ra lỗi:", str(e))

# try:
#     follower_element = driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]')
#     followers_text = follower_element.text  # Lấy toàn bộ nội dung văn bản của phần tử
#     followers_count = int(followers_text.split()[0])  # Tách số lượng người theo dõi (200)
#     print(f"Số lượng người theo dõi: {followers_count}")
# except Exception as e:
#     print("Không thể tìm thấy số lượng người theo dõi:", e)

# try:
#     like_element = driver.find_element(By.XPATH, '//a[contains(@href, "/friends_likes/")]')
#     likes_text = like_element.text  # Lấy toàn bộ nội dung văn bản của phần tử
#     likes_count = int(likes_text.split()[0])  # Tách số lượt thích (577)
#     print(f"Số lượt thích: {likes_count}")
# except Exception as e:
#     print("Không thể tìm thấy số lượt thích:", e)

# Lấy Page ID
# try:
#     element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/span')
#     content = element.text  # Lấy nội dung văn bản của phần tử
#     print("Nội dung bên trong:", content)
# except Exception as e:
#     print("Không tìm thấy phần tử hoặc lỗi:", str(e))

driver.quit()


