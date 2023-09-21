# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:29:32 2023

@author: g_s_s
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import seaborn as sns
import streamlit as st
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis

fm.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
plt.rcParams["font.size"] = 14
plt.rcParams['font.family'] = 'Taipei Sans TC Beta'
plt.close('all')
np.random.seed(123456)


ts0 = pd.Series(np.random.randint(-8,10,300))
ts0 = ts0.cumsum()
tsA = list(ts0[0:270])
for i in range(len(tsA)):
    tsA[i]=tsA[i]+30
tsB = list(ts0[10:280])
for i in range(len(tsB)):
    tsB[i]=tsB[i]+20+np.random.randint(-4,5)
tsC = list(pd.Series(np.random.randint(-7,10,270)).cumsum()+20)
df=pd.DataFrame({'A項指數':tsA,
                 'B項指數':tsB, 
                 'C項指數':tsC}, index=pd.date_range("1/1/2023", periods=270))
plt.figure()
df.plot()

st.header("初步想法：")
st.markdown("找到兩個**相關**的指數，如下圖中B項:red[**跟隨**]著A，那.....\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.line_chart(df)
st.divider()


plt.figure()
plt.title("相關係數(correlation coefficient)")
sns.heatmap(df.corr(), annot=True, fmt=".2f")

st.pyplot(plt)
st.divider()

plt.figure()
plt.title("不知道是甚麼的Dynamic Time Warping(DTW)")
ds = dtw.distance_matrix_fast(np.array(df.astype("float")).T)
sns.heatmap(pd.DataFrame(ds, 
                         columns=['A項指數', 'B項指數', 'C項指數'], 
                         index=['A項指數', 'B項指數', 'C項指數']), annot=True)

st.pyplot(plt)
st.divider()
plt.show()


st.caption('參考資料：')
st.caption('(1)如何用 DTW 在市場趨勢下時逆向獲利 http://18.178.46.40/info/detail.php?pid=11 ')
st.caption('(2).....')
