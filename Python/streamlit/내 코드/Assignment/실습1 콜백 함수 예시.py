import streamlit as st

# 콜백 함수 정의
def check_age(name, gender):
    user_age = st.session_state.user_age  # session_state를 통해 현재 사용자의 나이를 가져옵니다.
    if user_age < 20:
        st.write(f'{name}님은 미성년자이십니다. 성별: {gender}. 회원가입을 하기 위해서는 부모의 동의가 필요합니다.')
    else:
        st.write(f'{name}님, 성별: {gender}, 어서오세요!')

st.header('간단한 텍스트 기반 정보 표시 앱', divider='rainbow')

user_name = st.text_input('이름을 입력하세요', value='name', max_chars=20)
user_gender = st.radio('성별을 선택하세요', options=['남자', '여자'], index=0, horizontal=True,
                    key=1, help='성별을 선택하세요')
# 콜백 함수에 args와 kwargs를 사용하여 추가 인자 전달
user_age = st.number_input('나이를 입력하세요', value=15, min_value=0, max_value=999, key='user_age', on_change=check_age, args=(user_name,), kwargs={'gender': user_gender})