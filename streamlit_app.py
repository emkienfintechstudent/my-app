import streamlit as st
import numpy as np
import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
import requests
import json
# # URL API của Unwrangle
# url = "https://data.unwrangle.com/api/getter/"

# # Tham số cho yêu cầu API
# params = {
#     "platform": "amazon_search",  # Nền tảng Amazon với kiểu dữ liệu tìm kiếm
#     "search": "robot+vacuum+cleaner",  # Từ khóa tìm kiếm
#     "country_code": "us",  # Quốc gia USA
#     "page": 1,  # Số trang
#     "api_key": "c740d847c201b46a93f7c5135186e0f2c496df88"  # API Key của bạn
# }

# Gửi yêu cầu GET tới API
# response = requests.get(url, params=params)

# # Kiểm tra trạng thái yêu cầu
# if response.status_code == 200:
#     # Chuyển đổi phản hồi JSON thành đối tượng Python
#     data = response.json()
#     # In kết quả ra màn hình
#     print(data)
# else:
#     print(f"Yêu cầu không thành công, mã lỗi: {response.status_code}")
#     print(response.text)
# for i in data:
#     print(data['results'])
# with open('products_data.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data['results'], json_file, ensure_ascii=False, indent=4)   
# with st.expander('Data'):
#   st.write('**Raw data**')
#   df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
#   df
#   st.write('**X**')
#   X_raw = df.drop('species', axis=1)
#   X_raw
#   st.write('**Y**')
#   X_raw = df['species']
#   X_raw
# with st.expander('Data visualization'): 
#     st.scatter_chart(
#         data = df,
#         x="bill_length_mm",
#         y="body_mass_g",
#        color='species' 
#     )
with open('products_data.json', 'r', encoding='utf-8') as json_file:
    products_data = json.load(json_file)
print(products_data)

for product in products_data:
    print(product)
    break
df = pd.DataFrame(columns = [
    "name", 
    "url", 
    "thumbnail", 
    "rating", 
    "total_ratings", 
    "price", 
    "currency", 
    "currency_symbol", 
    "is_sponsored", 
    "past_month_bought"
])
with st.expander('Data visualization'): 
    for product in products_data:
          df.loc[len(df)]  = product
    a= df.drop(columns=["url", "thumbnail","currency_symbol", 
    "is_sponsored"])
    a