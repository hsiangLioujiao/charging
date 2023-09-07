import streamlit as st
import pandas as pd
from PIL import Image


st.title('充電站')
st.subheader("資料來源：")
image = Image.open('open_data.PNG')
st.image(image)
st.divider()

option = st.selectbox('請選擇電動車充電位置的資料來源：',
                      ('台灣糖業公司_加油站供電動車充電服務營業據點',
                       '台灣中油股份有限公司_提供電動車充電服務加油站',
                       '台灣中油股份有限公司_土地出租給充電樁業者營運加油站',
                       '嘉義市電動汽車充電站'))
st.write('目前顯示的是：', option)

if option == '台灣糖業公司_加油站供電動車充電服務營業據點':
    url="https://www.taisugar.com.tw/upload/UserFiles/%E5%8F%B0%E7%81%A3%E7%B3%96%E6%A5%AD%E5%85%AC%E5%8F%B8_%E5%8A%A0%E6%B2%B9%E7%AB%99%E4%BE%9B%E9%9B%BB%E5%8B%95%E8%BB%8A%E5%85%85%E9%9B%BB%E6%9C%8D%E5%8B%99%E7%87%9F%E6%A5%AD%E6%93%9A%E9%BB%9E.csv"
    df=pd.read_csv(url)
    df=df[['GPS定位座標東經度', 'GPS定位座標北緯度']]
elif option == '台灣中油股份有限公司_提供電動車充電服務加油站':
    url="https://www3.cpc.com.tw/opendata_d00/%E5%8F%B0%E7%81%A3%E4%B8%AD%E6%B2%B9%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8_%E6%8F%90%E4%BE%9B%E9%9B%BB%E5%8B%95%E8%BB%8A%E5%85%85%E9%9B%BB%E6%9C%8D%E5%8B%99%E5%8A%A0%E6%B2%B9%E7%AB%99.csv"
    df=pd.read_csv(url)
    df=df[['經度', '緯度']]
elif option == '台灣中油股份有限公司_土地出租給充電樁業者營運加油站':
    url="https://www3.cpc.com.tw/opendata_d00/%E5%8F%B0%E7%81%A3%E4%B8%AD%E6%B2%B9%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8_%E5%9C%9F%E5%9C%B0%E5%87%BA%E7%A7%9F%E7%B5%A6%E5%85%85%E9%9B%BB%E6%A8%81%E6%A5%AD%E8%80%85%E7%87%9F%E9%81%8B%E5%8A%A0%E6%B2%B9%E7%AB%99.csv"
    df=pd.read_csv(url)
    df=df[['經度', '緯度']]
elif option == '嘉義市電動汽車充電站':
    url="https://data.chiayi.gov.tw/opendata/api/getResource?oid=b1374d17-e503-49e1-9406-af2d323807f4&rid=14061c83-6aaf-4c54-8a1c-59c891eabda7"
    df=pd.read_csv(url)
    df=df[['經度', '緯度']]

df.columns=['lon', 'lat']
st.map(df)
st.write(url)
st.write("\n")
