from flask import Flask, redirect, request, render_template
import requests

app = Flask(__name__)

# Facebook App Configuration
APP_ID = "761640836136928"  # Thay bằng App ID của bạn
APP_SECRET = "8f1a1307eec6b77835f2376d8e995a80"  # Thay bằng App Secret của bạn
REDIRECT_URI = "https://8326-14-186-87-56.ngrok-free.app/callback"
  # Đảm bảo trùng khớp với cấu hình trong Facebook App

@app.route('/')
def home():
    """
    Trang chủ hiển thị nút Đăng nhập bằng Facebook
    """
    fb_login_url = (
        f"https://www.facebook.com/v21.0/dialog/oauth"
        f"?client_id={APP_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=pages_manage_posts,pages_manage_engagement,pages_read_engagement,pages_show_list"
    )


    return render_template('index.html', fb_login_url=fb_login_url)


@app.route('/callback')
def callback():
    """
    Xử lý callback sau khi người dùng cấp quyền
    """
    # Lấy mã code từ query string
    code = request.args.get('code')
    if not code:
        return "Đăng nhập thất bại hoặc bị hủy.", 400

    # Trao đổi mã code để lấy Access Token
    token_url = "https://graph.facebook.com/v21.0/oauth/access_token"
    params = {
        "client_id": APP_ID,
        "redirect_uri": REDIRECT_URI,
        "client_secret": APP_SECRET,
        "code": code,
    }
    response = requests.get(token_url, params=params)

    if response.status_code != 200:
        return "Lỗi khi lấy Access Token", 400

    # Trích xuất Access Token từ phản hồi
    access_token = response.json().get('access_token')

    # Lấy thông tin người dùng từ Facebook
    user_info_url = f"https://graph.facebook.com/v17.0/me?access_token={access_token}"
    user_info_response = requests.get(user_info_url)

    if user_info_response.status_code != 200:
        return "Lỗi khi lấy thông tin người dùng", 400

    # Hiển thị thông tin người dùng
    user_info = user_info_response.json()
    user_id = user_info.get('id')

    url_page = f"https://graph.facebook.com/v17.0/{user_id}/accounts?access_token={access_token}"
    user_page_response = requests.get(url_page)
    if user_page_response.status_code != 200:
        return "Lỗi khi lấy thông tin người dùng", 400
    page_info = user_page_response.json()
    access_token_page = page_info.get('data')[0].get('access_token')

    # access_token_page = 'EAAK0tVN7ZCZBABO3Mwg6Di46Y5IRqzd9JILEvKg0IJW9fmde5j18XxNyVwZAjo38c9d0lFOMnF7ahHudSBvjU7AYpra6RZBNP67hoNzIlQnyN5p3yUd22mZAyvUmbi1WJlGx8jlZBYYs1RrXEQFVdwbPZCYNZAY6GyfcYgdoMW7FYZCkvdd1FVDSZCC6uhG0ZBAExJu'
    url_page_id = f"https://graph.facebook.com/v17.0/me?access_token={access_token_page}"
    id_page_response = requests.get(url_page_id)
    if id_page_response.status_code != 200:
        print("Lỗi khi lấy thông tin người dùng")
    page_id_info = id_page_response.json()
    page_id = page_id_info.get('id')



    # Truyền access_token và thông tin người dùng đến template
    return render_template('callback.html', access_token=access_token_page, user_id=page_id)

if __name__ == '__main__':
    app.run(debug=True)