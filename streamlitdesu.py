# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:03:04 2021

@author: aika takeda
"""

import streamlit as st
st.title("一押しのラーメン屋さん教えてください")
st.write("私の名前は竹田です")
st.write("私のおすすめはオランダ軒です")
text=st.text_input("あなたのおすすめを教えてください")
"あなたのおすすめのラーメン屋さんは,",text,"です"
point=st.slider("ざっと点数をつけるなら？",0,100,50)
"点数:",point
option=st.selectbox("何系らーめんですか？",list(["醤油","味噌","豚骨","煮干し","塩","鶏白湯","つけ麺"]))
"あなたが選択したのは、",option,"です"
st.write("ちなみにオランダ軒の写真です")
from PIL import Image    
img=Image.open("オランダ軒.jpg")
st.image(img,caption="醤油チャーシュー麺",use_column_width=True)   
st.write("生姜がきいて最高です")
