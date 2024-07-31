import streamlit as st

import pandas as pd
from io import BytesIO

st.title("다운로드 버튼")

st.code('st.download_button(label=다운로드 버튼 이름,' 
        +'data = open함수로 여는 데이터,'
        +'file_name=파일 상대경로명,'
        +'mime=text/plain, html, css 등등)')

st.subheader("예제 1. 텍스트 파일 다운로드")

folder= '../data/'

with open (folder + '서연의_이야기.txt', encoding='utf-8') as f: # 텍스트 파일은 인코딩
    data = f.read()
    st.download_button(
        label = '텍스트 파일 다운로드', 
        data = data, 
        file_name = '서연의_이야기.txt',
        mime = 'text/plain'
        )
    
st.subheader("예제 2. 이미지 파일 다운로드")
with open(folder+'ShinYoonbok.png','rb') as f: # 사진, 동영상 이진 파일 읽기 모드 지정
    data = f.read()
    st.download_button(
        label = '이미지 파일 다운로드',
        data = data,
        file_name = 'ShinYoonbok.png',
        mime = 'image/png'
        )
    
st.subheader("예제 3. 오디오 파일 다운로드")
with open(folder+'서연의_하루_TTS_배경음악_short.mp3', 'rb') as f:
    data = f.read()
    st.download_button(
        label = '오디오 파일 다운로드',
        data = data,
        file_name = '서연의 하루 배경음악(TTS).mp3',
        mime = 'audio/mp3'
    )