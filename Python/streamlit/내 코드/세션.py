# 목적 : 스트림릿의 코드의 동작을 제어

# 스트림릿은 코드를 생성한 후 앱을 재실행하거나, 입력 위젯을 조작하면 전체 코드를 처음부터 끝까지 다시 실행하는 구조.

# 코드가 한번 실행된 상태를 세션이라고 한다.

# 일반적인 변수는 세션간 공유되지 않는다.

# 세션 상태(session_state)를 이용해 해결 가능 : 이전 세션에서 변경한 상태를 저장하고 그대로 유지

import streamlit as st

st.title('세션과 콜백')

# 세션 상태 초기화 : 기본 구조 key - value

if 'count' not in st.session_state:
    st.session_state['count'] = 0

if 'registed' not in st.session_state:
    st.session_state['registered'] = []

# 텍스트 입력 위젯
user_input = st.text_input('이름', value='이름을 입력하세요', key='name')

# 버튼 입력 위젯
clicked = st.button('등록', key='button')

if clicked:
    st.session_state['count'] += 1
    st.write('버튼 클릭 : ', st.session_state['count'])
    
    # name = st.session_state['name']
    st.session_state['registered'].append(user_input)
    st.write('등록된 이름 : ', st.session_state['registered'])
    
'''
콜백(CallBack) : 특정 함수를 다른 함수의 인자로 전달하고,
미리 정해진 조건을 충족하거나 이벤트가 발생했을때 해당 함수를 호출하는 패턴입니다.
이때 전달하는 함수를 콜백 함수라고 한다.
'''

st.header('callback', divider='rainbow')

    
# 라디오 버튼
radio_options = ['Python', 'Java', 'C++']
radio_selected = st.radio('가장 좋아하는 언어는?', radio_options)

# 버튼 위젯
def btn_callback(lang):
    st.session_state['lang'] = lang
    
click = st.button('선택', on_click=btn_callback, args=(radio_selected,))

if click:
    st.write(f"저는 {st.session_state.get('lang')}을 좋아합니다.")