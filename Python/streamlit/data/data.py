# import streamlit as st

# # 3. 데이터 요소

# # st.dataframe
# # st.dataframe : 데이터프레임 출력

# import pandas as pd

# st.subheader("메뉴판 (가로 555 세로 255 dataframe)")
# df_menu = pd.DataFrame({"메뉴명": ["짜장면", "짬뽕", "탕수육", "볶음밥"],
#                         "가격": [5000, 6000, 12000, 7000]})
# df_menu.index = range(1, len(df_menu)+1)

# # use_container_width = True : 컨테이너 너비에 맞춤
# st.dataframe(df_menu, width = 555, height = 255)

# # st.table
# # st.table : 표 출력 (정적인 데이터)

# st.subheader("메뉴판(table : 렌더링이 더 빠름)")
# list_menu = [["짜장면", 5000], ["짬뽕", 6000], ["탕수육", 12000], ["볶음밥", 7000]]
# st.table(list_menu) # 리스트 출력

import streamlit as st
import pandas as pd

st.title("영화 관리 시스템")
st.header("영화 목록")
st.subheader("추천 영화 목록")
st.markdown("**다음은 추천 영화 목록과 각 영화의 감독 및 개봉연도입니다.**")
movie = pd.DataFrame({"영화":["기생충", "라라랜드", "포레스트 검프", "타이타닉"],
"개봉연도":["2019년", "2016년", "1994년", "1997년"],
"감독":["봉준호", "데이미언 셔젤", "로버트 저메키스", "제임스 카메론"]})
movie.index = range(1, len(movie)+1)
st.dataframe(movie, use_container_width=True)
video_url = "https://youtu.be/jBdRhhSt3Bc"
st.video(video_url)