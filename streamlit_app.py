import streamlit as st
from PIL import Image
import datetime
import time

# Thiết lập tiêu đề và giao diện
st.set_page_config(page_title="🎉 Birthday Wishes 🎉", page_icon="🎂", layout="centered")

# Tạo nền gradient cho ứng dụng
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hiển thị tiêu đề với phông chữ đặc biệt
st.markdown(
    "<h1 style='text-align: center; color: #f36b6b; font-family: fantasy;'>🎉 Chúc Mừng Sinh Nhật! 🎉</h1>",
    unsafe_allow_html=True
)

st.markdown("<h2 style='text-align: center; font-family: cursive;'>Ngày đặc biệt của bạn đã đến rồi!</h2>", unsafe_allow_html=True)

# Nhập tên người được chúc mừng và ngày sinh
name = st.text_input("Nhập tên của bạn:", "Người Bạn Đặc Biệt", help="Nhập tên của người mà bạn muốn chúc mừng.")
birthday = st.date_input("Nhập ngày sinh của bạn:", datetime.date.today())

# Hiển thị lời chúc mừng sinh nhật với hoạt cảnh đẹp mắt
if st.button("🎈 Chúc Mừng Sinh Nhật 🎈"):
    st.markdown(
        f"<h2 style='text-align: center; color: #ff6347; font-family: monospace;'>🎂 Chúc mừng sinh nhật {name}! 🎂</h2>",
        unsafe_allow_html=True
    )
    st.balloons()
    st.success(f"Chúc {name} luôn mạnh khỏe, hạnh phúc và gặp nhiều may mắn trong cuộc sống!")

# Thêm hình ảnh chúc mừng và hoạt cảnh động
if st.button("🎁 Hiển Thị Hình Ảnh Chúc Mừng 🎁"):
    image = Image.open("happy_birthday.jpg")  # Thay thế bằng đường dẫn đến ảnh của bạn
    st.image(image, caption=f"🎉 Happy Birthday, {name}! 🎉", use_column_width=True)
    st.markdown(
        "<h3 style='text-align: center; color: #8a2be2;'>Chúc bạn một ngày sinh nhật thật vui vẻ và ý nghĩa!</h3>",
        unsafe_allow_html=True
    )
    
# Thêm nút phát nhạc và lời nhắn gửi đặc biệt
st.markdown("<h3 style='text-align: center; color: #2e8b57; font-family: sans-serif;'>Nhấn nút dưới để nghe nhạc chúc mừng 🎵</h3>", unsafe_allow_html=True)
if st.button("🎵 Phát Nhạc 🎵"):
    st.audio("happy_birthday.mp3")  # Thay thế bằng đường dẫn tới tệp âm thanh của bạn
    st.markdown("<h3 style='text-align: center; font-family: sans-serif; color: #ff4500;'>Đón nhận những khoảnh khắc tuyệt vời trong ngày đặc biệt này nhé!</h3>", unsafe_allow_html=True)

# Nhúng video chúc mừng sinh nhật
st.markdown("<h3 style='text-align: center; color: #8b0000;'>🎥 Video Chúc Mừng Sinh Nhật 🎥</h3>", unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Thay bằng đường dẫn video bạn muốn

# Hiển thị đồng hồ đếm ngược đến sinh nhật
st.markdown("<h3 style='text-align: center; font-family: serif;'>⏳ Đếm Ngược Đến Sinh Nhật Của Bạn ⏳</h3>", unsafe_allow_html=True)
current_time = datetime.datetime.now()
birthday_time = datetime.datetime.combine(birthday, datetime.datetime.min.time())
if birthday_time < current_time:
    birthday_time = birthday_time.replace(year=current_time.year + 1)

countdown = birthday_time - current_time
st.write(f"Chỉ còn {countdown.days} ngày {countdown.seconds // 3600} giờ {countdown.seconds % 3600 // 60} phút đến sinh nhật của bạn!")

# Footer với lời cảm ơn
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
    <h4 style="font-family: sans-serif; color: #3CB371;">🎉 Cảm ơn bạn đã ghé thăm! Chúc bạn một ngày tuyệt vời! 🎉</h4>
    </div>
    """,
    unsafe_allow_html=True
)
