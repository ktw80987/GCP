import streamlit as st

st.header(
    '간단한 텍스트 기반 정보 표시 앱', divider='rainbow'
)

user_name = st.text_input('이름을 입력하세요', value='name', max_chars=20, key=0)
user_gender = st.radio('성별을 선택하세요', options=['남자', '여자'], index=0, horizontal=True,
                    key = 1, help='성별을 선택하세요')
user_age = st.number_input('나이를 입력하세요', value=15, min_value=0, max_value=999, key=2)

if user_age<20:
        st.write(f'{user_name}님은 미성년자이십니다. 회원가입을 하기 위해서는 부모의 동의가 필요합니다.')
else:
        st.write(f'{user_name}님 어서오세요!')