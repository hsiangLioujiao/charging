# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:31:21 2023

@author: g_s_s
"""
import streamlit as st

k = st.text_input('請輸入一個整數：', '10')
k = int(k)

#用if及%
s=0
st_s=""
for i in range(1,k+1):
    if (i%2 ==0):
        print(i, ' ', end='')
        st_s=st_s+str(i)+", "
        s=s+i
print()
st.caption(st_s)
print("從2, 4, 6, ...累加到%d的合是%d" % (k,s))
st.write('從2, 4, 6, ...累加到%d的合是%d' % (k,s))
print()


#不用if
sum=0
for i in range(2,k+1,2):
    print(i,' ',end='')
    sum=sum+i
print()
print("從2, 4, 6, ...累加到%d的合是%d" % (k,sum))
print("\n")
