import streamlit as st

# 스트림릿 버튼 입력 예제

st.title("스트림릿 버튼 입력 예제")

onclick1 = st.button('버튼1')

st.write('버튼1 을 클릭하셨습니다:', onclick1)

onclick2 = st.button('버튼2')
st.write('버튼2 을 클릭하셨습니다:', onclick2)
if onclick2:
    st.write('버튼을 클릭하셨습니다.')
else:
    st.write('버튼을 클릭하지 않았습니다.')