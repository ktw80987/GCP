import streamlit as st
import datetime
from io import StringIO

st.title('대표적 입력 위젯')
st.header('텍스트 입력', divider='rainbow')
st.code('st.text_input(label, value="", max_chars=None, type="default")')
description1 = st.caption('type : 입력 텍스트의 형식, '
+'value : 입력 텍스트의 초기값, '
+'max_chars : 입력 텍스트의 최대 길이, '
+'type : 입력 텍스트의 형식')

user_id = st.text_input('아이디', value = '아이디를 입력하세요', max_chars=20, type='default')
user_password = st.text_input('비밀번호', '비밀번호를 입력하세요', type='password')
if user_id == 'kim':
    if user_password == '1234':
        st.write('로그인 성공')
    else:
        st.write('비밀번호가 틀렸습니다.', unsafe_allow_html=True)
else:
    st.write('없는 아이디 입니다.')
    
st.divider()

st.header('text_area 입력', divider='rainbow')
txt=st.text_area('text area 입니다', '최초 표시되는 값', max_chars=200, height=100, key='text_area')
st.write(f'현재 area에 사용된 문자 개수 : {len(txt)}개')

st.divider()

prompt = st.chat_input(placeholder='메시지를 입력하세요', max_chars= 200, disabled=False, on_submit=True)
if prompt:
    st.write(f'사용자 입력: {prompt}')
    
st.divider()

st.header('날짜 입력', divider='rainbow')
st.code('st.date_input(label, value="default", min_value, max_value, format=YYYY/MM/DD, disabled=False)')
description2 = st.caption('label : 입력 위젯의 라벨,' 
+'value : 초기값,' 
+'min_value : 최소값,' 
+'max_value : 최대값,'
+'format : 날짜 형식,'
+'disabled : 비활성화 여부')

date = st.date_input('날짜를 입력하세요', value = datetime.date.today(), min_value=datetime.date(2021, 1, 1), max_value=datetime.date(2024, 12, 31), format='YYYY-MM-DD')
st.write(f'선택한 날짜 : {date}')

st.divider()

st.header('파일 올리기 형식 만들기', divider='rainbow')
st.code('st.file_uploader(label, type = txt, csv 등등  accept_multiple_files=False)')

# type : 업로드 가능한 파일 형식
# accept_multiple_files : 여러 파일을 업로드할 수 있는지 여부

upload_file = st.file_uploader('텍스트 파일을 업로드하세요', type='txt', accept_multiple_files=False)
upload_file2 = st.file_uploader('음악 파일을 업로드 하세요', type='mp3', accept_multiple_files=False)

if upload_file is not None:
    stringio = StringIO(upload_file.getvalue().decode('utf-8'))
    string_data = stringio.read()
    st.write(string_data[:20])
    
if upload_file2 is not None:
    byte_data = upload_file2.getvalue()
    st.write(byte_data[:20])
    
upload_files = st.file_uploader('여러 파일을 업로드하세요', accept_multiple_files=True)
if upload_files is not None:
    for file in upload_files:
        st.write(file.name)