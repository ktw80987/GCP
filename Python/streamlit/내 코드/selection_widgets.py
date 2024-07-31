import streamlit as st

st.header('체크 박스', divider='rainbow')

st.code("st.checkbox(label='체크박스 이름', value = True/False)")

'''
label : 체크박스 옆에 표시될 문자
value : 체크박스이 초기값, 기본값은 False

return 값은 True / False
'''

checked1 = st.checkbox(label = '체크박스1', value = True) # True시 박스에 체크 돼있습니다.
checked2 = st.checkbox(label = '체크박스2', value = False) # False시 체크가 안되있는 빈 칸입니다.

st.write('체크박스1 상태: ', checked1)
st.write('체크박스2 상태: ', checked2)

st.markdown('---')

st.header('라디오 버튼', divider='rainbow')
'''
미리 정의된 옵션 중 하나를 선택할 수 있는 라디오 버튼
'''

st.code("st.radio(label='라디오 버튼 이름', options(리스트)=['옵션1', '옵션2', '옵션3'], index=0(체크 돼 있는 항목, 기본값=0))")

st.markdown('''
<!--
<div>
label : 라디오 버튼에 표시할 문자열
options: 선택항목 라벨을 담고 있는 리스트 또는 튜플, 선택항목 라벨 갯수만큼 라디오 버튼 선택항목이 생성
index : 체크 돼 있는 항목, , default = 0
horizontal : 선택 항목 라벨 배치 순서, True : 가로 방향, False : 세로 방향. default = False
</div> 
-->
''', unsafe_allow_html=True)

radio1_options = ['10', '20', '30', '40', '50']
radio1_selected = st.radio(label = '(1) (5+5)*1은?', options = radio1_options, index = 0, horizontal = True)
st.write('답 : ', radio1_selected)

radio2_options = ['1', '2', '3', '4', '5']
radio2_selected = st.radio(label = '(2) (5+5)*2은?', options = radio2_options, index = 0, horizontal = True)
st.write('답 : ', radio2_selected)


st.divider()

st.header('셀렉트 박스: blue[selecteBox]', divider='rainbow')

st.markdown(''' st.selectbox(label, options(리스트), index=0) ''')

selectbox1_options = [ '한식', '중식', '일식', '양식', '분식']
your_option1 = st.selectbox("selectbox1 내일 뭐 먹지?", selectbox1_options)
st.write('선택한 메뉴 : ', your_option1)

selectbox2_options = ['-'*50, '한식', '중식', '일식', '양식', '분식'] 
your_option2 = st.selectbox("selectbox2 내일 뭐 먹지?", selectbox2_options, index = 0)

if your_option2 == selectbox2_options[0]:
    pass
else:
    st.write('선택한 메뉴 : ', your_option2)