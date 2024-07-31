import streamlit as st
from PIL import Image

st.sidebar.title('Siderbar')
st.sidebar.header('로그인', divider='rainbow')
user_id=st.sidebar.text_input('ID')
user_password=st.sidebar.text_input('Password', type='password')

st.sidebar.header('selectbox', divider='rainbow')
selectbox_options=st.sidebar.selectbox('그림', ['그림1', '그림2', '그림3', '그림4'])


if selectbox_options is None:
    pass
else:
    st.sidebar.write(f'{selectbox_options}를 선택하셨습니다.')
    
st.divider()
st.title('메인 화면')
folder = '../data/'
image_files = ['Vermeer.png', 'Gogh.png', 'Munch.png', 'ShinYoonbok.png']

selectbox_options_index = selectbox_options.index(selectbox_options)

if selectbox_options_index != 0 :
    image_files = [image_files[selectbox_options_index-1]]
    image_local = Image.open(folder + image_files)
    st.image(image_local)
    
