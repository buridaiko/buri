from http.client import PROXY_AUTHENTICATION_REQUIRED
import streamlit as st
import numpy as np
import pandas as pd
from sympy import python
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('ブログレスバーの表示')
'Srart!!!'
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!'

left_column,right_colum=st.beta_columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_colum.write('ここは右カラム')

expander=st.beta_expander('問い合わせ')
expander.write('お問い合わせを書く')
#text=st.text_input('あなたの趣味を教えてください')
#condtion=st.slider('あなたの今の調子は？',0,100,50)

#'あなたの趣味は、',text
#'コンディション:',condtion

#if st.checkbox('Show Image'):
    #img=Image.open('sample,jpg')
    #st.image(img,caption='バイク',use_column_width=True)