import streamlit as st
from PIL import Image

st.title('메인 화면 분할')

st.header('컬럼으로 화면 분할', divider='rainbow')
st.code('st.columns(spec)')

st.subheader(' 1) 2개의 컬럼으로 분할 :blue[너비는 같게]')
[col1, col2] = st.columns(2)

with col1:
    col1.markdown(':rainbow[영상1]', unsafe_allow_html=True)
    col1_url='https://youtu.be/1Fgzc8nyWr4?list=RD1Fgzc8nyWr4'
    st.video(col1_url)

with col2:
    col2.markdown(':rainbow[영상2]', unsafe_allow_html=True)
    col2_url='https://youtu.be/iILJvqrAQ_w?list=RD1Fgzc8nyWr4'
    st.video(col2_url)
    
st.divider()
st.subheader(' 2) 3개의 컬럼으로 분할 :blue[-너비는 서로 다르게]', divider='rainbow')
columns = st.columns([1, 2, 3])
print(columns)
folder = './data/'
image_files = ['dog.png', 'cat.png', 'bird.png']
image_captions = ['강아지', '고양이', '새']

for i in range(len(columns)):
    with columns[i]:
        image_local = Image.open(folder + image_files[i])
        st.image(image_local, caption=image_captions[i])
        
st.divider()

st.header('탭으로 화면 분할', divider='rainbow')
st.code('st.columns(spec)')
# spec : 각 tab의 이름을 리스트로 지정

tab1, tab2 = st.tabs(['Tab1', 'Tab2'])

with tab1:
    st.image(Image.open(folder + 'dog.png'), caption='강아지')
    
with tab2:
    st.image(Image.open(folder + 'cat.png'), caption='고양이')