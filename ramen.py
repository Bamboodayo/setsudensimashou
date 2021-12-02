# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 03:54:27 2021

@author: aika takeda
"""
import gspread
import folium
import googlemaps
import time
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
import random


m='0'
r='0'

st.title("ラーメン愛好者の集い")
a=st.selectbox("どれを表示しますか",list(["Googleフォーム","ラーメンマップ","ラーメン写真館","おまけ：ラーメン占い"]))

if a=="Googleフォーム":
    st.write('こちらをクリックしてください','https://forms.gle/Tdj7zjuKfyWswdKQ9')
    link='https://forms.gle/Tdj7zjuKfyWswdKQ9'
    st.sidebar.markdown(link, unsafe_allow_html=True)

elif a == 'ラーメン写真館' :
    st.write("ラーメン写真館です")
    st.write("作者の気分次第、適宜追加していきます")
    col1,col2,col3=st.columns(3)
    with col1:
        img=Image.open("オランダ軒.jpg")
        st.image(img,caption="オランダ軒",use_column_width=True) 
    with col2:
        img=Image.open("さくら.jpeg")
        st.image(img,caption="佐蔵",use_column_width=True) 
    with col3:
        img=Image.open("丸山中華蕎麦店.jpeg")
        newimg=img.rotate(90)
        st.image(newimg,caption="丸山中華蕎麦店",use_column_width=True) 
    col1,col2,col3=st.columns(3)
    with col1:
        img=Image.open("開智.jpeg")
        st.image(img,caption="開智の学食",use_column_width=True) 
    with col2:
        img=Image.open("にぼしや.jpeg")
        newimg=img.rotate(270) 
        st.image(newimg,caption="つけ麺　弐☆゛屋",use_column_width=True) 
    with col3:
        img=Image.open("どんく.jpeg")
        st.image(img,caption="どんく",use_column_width=True) 
    col1,col2,col3=st.columns(3)
    with col1:
        img=Image.open("邦心らーめん松本駅前店.jpg")
        st.image(img,caption="邦心らーめん松本駅前店",use_column_width=True) 
    with col2:
        img=Image.open("めん丸　身延店.jpg")
        st.image(img,caption="めん丸　身延店",use_column_width=True) 
    with col3:
        img=Image.open("よってこや.jpg")
        st.image(img,caption="よってこや",use_column_width=True) 
    

elif a=="ラーメンマップ":
    
     st.write("ラーメンマップです")

     gc = gspread.service_account(filename="./service_account.json")
     sh = gc.open("raramen")
     h=st.text_input('何件表示させますか？')
     if len(h)>0 and len(a)>=5 :
         googleapikey = 'AIzaSyBuoDH9eBgTU9zA3U0iARo4It-S2zb3seg'
         gmaps = googlemaps.Client(key=googleapikey)
         m=folium.Map(location=[35.9616396,139.7106896],zoom_start= 16)  
         for i in range(2,int(h)+2):
             e='C'+str(i)
             locate=sh.sheet1.get(e)
             gmap_list = gmaps.geocode(str(locate))
             ll = gmap_list[0]["geometry"]["location"]
             time.sleep(0.6)
             folium.Marker(location=[ll["lat"],ll["lng"]]).add_to(m)
             m.save('nagano3.html')
     else:
         pass
     folium_static(m, width=700, height=500) 
else :
    st.write("おまけ：ラーメン占いです")
    st.write("今日のあなたにおすすめのラーメンは・・・")
    kuji=["オランダ軒","よってこや","カナキン亭本舗藤枝本店","めん丸　身延店","邦心らーめん松本駅前店","丸山中華蕎麦店","どんく","つけ麺　弐☆゛屋","佐蔵","開智食堂"]
    r = random.choice(kuji) 
    st.header(r)
    if r =="オランダ軒" :
        col1,col2=st.columns(2)
        with col1:
            img=Image.open("オランダ軒.jpg")
            st.image(img,caption="オランダ軒",use_column_width=True) 
        with col2:
            st.write("住所")
            st.write("埼玉県さいたま市岩槻区東岩槻6-5-3 イケダ第一コーポ 1F 2号室")
    elif r =='よってこや' :
        col1,col2=st.columns(2)
        with col1:
            img=Image.open("よってこや.jpg")
            st.image(img,caption="よってこや",use_column_width=True)
        with col2:
            st.write("住所")
            st.write("静岡県静岡市駿河区石田3丁目10-3")
    elif r == 'カナキン亭本舗藤枝本店' :
        col1,col2=st.columns(2)
        with col1:
            img=Image.open("カナキン亭本舗藤枝本店.jpg")
        with col2 :
            st.write("住所")
            st.write("静岡県藤枝市駅前3丁目2-17")
    elif r == 'めん丸':
        col1,col2=st.columns(2)
        with col1:
            img=Image.open("めん丸　身延店.jpg")
            st.image(img,caption="めん丸　身延店",use_column_width=True)
        with col2:
            st.write("住所")
            st.write("山梨県南巨摩群身延町下山231-260")
    elif r == '邦心らーめん松本駅前店' :
        col1,col2=st.columns(2)
        with col1:
            img=Image.open("邦心らーめん松本駅前店.jpg")
            st.image(img,caption="邦心らーめん松本駅前店",use_column_width=True)
        with col2:
            st.write("住所")
            st.write("長野県松本市中央1丁目5-11")
    elif r == '丸山中華蕎麦店':
        col1,col2=st.columns(2)
        with col1:
            img=Image.open("丸山中華蕎麦店.jpeg")
            st.image(newimg,caption="丸山中華蕎麦店",use_column_width=True)
        with col2:
            st.write("住所")
            st.write("長野県松本市里山辺1619-5")
    elif r == '丸山中華蕎麦店':
        col1,col2=st.columns(2)
        with col1:
            img=Image.open("どんく.jpeg")
            st.image(img,caption="どんく",use_column_width=True)
        with col2:
            st.write("住所")
            st.write("長野県長野市北石堂町1398-1")
    elif r == 'つけ麺　弐☆゛屋' :
        col1,col2=st.columns(2)
        with col1:
            img=Image.open("にぼしや.jpeg")
            st.image(newimg,caption="つけ麺　弐☆゛屋",use_column_width=True)
        with col2:
            st.write("住所")
            st.write("埼玉県さいたま市北区日進町2-1127 小池ビル 1F")
    elif r == '佐蔵' :
        col1,col2=st.columns(2)
        with col1:
            img=Image.open("さくら.jpeg")
            st.image(img,caption="佐蔵",use_column_width=True)
        with col2:
            st.write("住所")
            st.write("長野県松本市中央1-20-26")
    elif r== '開智':
        col1,col2=st.columns(2)
        with col1:
            img=Image.open("開智.jpeg")
            st.image(img,caption="開智の学食",use_column_width=True)
        with col2:
            st.write("住所")
            st.write("埼玉県さいたま市岩槻区徳力186")
    else :
        pass