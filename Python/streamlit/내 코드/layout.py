import streamlit as st
import numpy as np
import time

st.title("스트림릿 컨테이너")
st.markdown('- 여러 요소를 담는 컨테이너를 생성하는 함수')
st.markdown('- 요소들을 그룹화하고 필요한 시점에서 표시, 숨길 수 있는 함수')

st.divider()
st.code('st.container(user_column_width, scrolls, expand, clear_on_reload)')

st.header('Container1-외부')
container = st.container()
container.write('1번째 생성한 컨테이너 외부')
st.write('컨테이너 외부에 출력')

st.divider()

st.header('Container2-내부')
container = st.container()
container.write('2번째 생성한 컨테이너 내부')
st.bar_chart(np.random.randn(50, 3))

st.divider()

st.header('Container3-내부')
container3 = st.container()
container3.write('3번째 생성한 컨테이너 내부')

st.divider()
st.header('st.empty()')
c4 = st.empty()
c4.text('4번째 생성한 컨테이너 내부')

time.sleep(3)