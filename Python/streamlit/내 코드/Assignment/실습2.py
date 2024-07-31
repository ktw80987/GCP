import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

st.title('데이터 시각화 어플리케이션')

upload_file = st.file_uploader('파일 업로드', type='csv')

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write('데이터 미리보기', df)
    
column = st.selectbox('위 데이터 프레임에 있는 열을 선택하세요', df.columns)

if column:
    fig, ax = plt.subplots()
    df[column].plot(bins=30, ax=ax)
    ax.set_title(f'{column} histogram')
    ax.set_xlabel(column)
    ax.set_ylabel('빈도수')
    ax.pyplot(fig)