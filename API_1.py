import requests
import pandas as pd
import json

# Thông tin bài viết
page_id = '535325259663598'  # ID của trang
access_token = 'EAAP6bri8RzYBO4G8L1LCyUqFUW92P0GZAqd2jV14wtKyFhkSQWGlf1dXp0C9JEor8UiJPyOUdbKyoj07aW7IZB04gWyA1DS4uXFxZBOpY66oKAaMIDML4QOMRMECqQDNlGAm5GrSY8u3Roa7dO1RCldvxWeQpHRi7oqEL4sZBZClJJRIdXwZCtqA8ZCShnrV01y9xhdDWoijHKyBQH7Cy3KDC1l'  # Thay bằng Access Token của bạn
post_id = '535325259663598_122095124456645438'
url = f"https://graph.facebook.com/v17.0/{post_id}/comments?fields=message,from,created_time&access_token={access_token}"
try:
    # Gửi yêu cầu GET đến Facebook Graph API
    response = requests.get(url)
    
    # Kiểm tra mã trạng thái của phản hồi
    if response.status_code == 200:
        # Chuyển đổi dữ liệu JSON thành Python object
        data = response.json()
        print(data.get('data')[0])
        print(len(data.get('data')))
        # Lấy danh sách bình luận
        
    else:
        print(f"Lỗi khi truy cập API: {response.status_code}, {response.text}")

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
