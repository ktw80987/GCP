import streamlit as st

st.title('Hello, it\'s Streamlit!')
st.sidebar.title('정보 등록')
st.sidebar.header('정보를 입력하세요', divider='rainbow')
user_name = st.sidebar.text_input('이름', max_chars=5, key='name')
user_age = st.sidebar.text_input('연령', key='age')

# 세션 상태 초기화
if 'name_list' not in st.session_state:
    st.session_state['name_list'] = []
if 'age_list' not in st.session_state:
    st.session_state['age_list'] = []

# 정보 등록 버튼
submit = st.sidebar.button('정보 등록')

if submit:
    if user_name and user_age is not None:
        st.session_state['name_list'].append(user_name)
        st.session_state['age_list'].append(user_age)
        
# 등록된 정보 출력
for name, age in zip(st.session_state['name_list'], st.session_state['age_list']):
    st.markdown(f'이름: **{name}**, 나이: **{age}**')

# 초기화 버튼
click = st.button('초기화')
if click:
    st.session_state['name_list'] = []
    st.session_state['age_list'] = []