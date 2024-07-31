import streamlit as st

st.code('st.camera_input(label, label_visibility="collapsed", type=\'jpeg\', key=None)')

st.markdown('### camera_input')
pic = st.camera_input('Take a picture', key=1)
if pic:
    st.image(pic)

img_buffer = st.camera_input('Take a picture', type='jpeg', key=2)
if img_buffer is not None:
    bytes_data = img_buffer.getvalue()
    st.write(type(bytes_data))