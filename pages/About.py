# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:29:32 2023

@author: g_s_s
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import streamlit as st

fm.fontManager.addfont('D:\\.data\\TaipeiSansTCBeta-Regular.ttf')
plt.rcParams["font.size"] = 14
plt.rcParams['font.family'] = 'Taipei Sans TC Beta'

plt.close('all')
np.random.seed(123456)
ts0 = pd.Series(np.random.randint(-8,10,300))
#ts0 = pd.Series(np.random.randint(-8,10,300), index=pd.date_range("1/1/2023", periods=300))
ts0 = ts0.cumsum()
tsA = list(ts0[0:270])
for i in range(len(tsA)):
    tsA[i]=tsA[i]+30
tsB = list(ts0[10:280])
for i in range(len(tsB)):
    tsB[i]=tsB[i]+20+np.random.randint(-4,5) 
df=pd.DataFrame({'A項指數':tsA, 'B項指數':tsB}, index=pd.date_range("1/1/2023", periods=270))
#上式中list()
plt.figure()
df.plot()

st.header("初步想法：")
st.write("找到兩個相關的指數，如下圖中B項跟隨著A，那.....")
st.line_chart(df)