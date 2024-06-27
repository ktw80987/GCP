# 데이터 출력

# 텍스트 요소, 미디어 요소, 데이터 요소
# 텍스트 요소 : 정보를 전달하고 설명
# 미디어 요소 : 이미지, 오디오, 비디오 파일을 출력
# 데이터 요소 : 데이터 프레임 및 테이블 형식으로 데이터를 표시

# import streamlit as st

# 1. 텍스트 요소
# title > header > subheader

# st.title : 가장 큰 제목
# str1 = "# :green[이것은] ***:red[st.title]*** :blue[입니다.]"
# st.markdown(str1)

#  st.header : 중간 제목
# str2 = "## 이것은 *:orange[st.header]* 입니다."
# st.markdown(str2)

# st.subheader : 가장 작은 제목
# str3 = "### 이것은 *:purple[subheader]* 입니다."
# st.markdown(str3)

# markdown : 일반 텍스테에 글자색, 글씨체 등의 시각효과

# markdown 일부 형식
# - 진하게(볼드) : **텍스트** / __텍스트__
# - 기울임(이탤릭) : *텍스트* / _텍스트_
# 색상 : color[텍스트] 형식 => red, green, blue, yellow, pink, ...
# - 취소선 : ~~텍스트~~

# st.text : 순수 문자 출력
# st.text("이것은 st.text 입니다.")

# st.caption : 표 아래에 설명을 추가
# st.title("~~st.title~~")
# st.caption("이것은 st.caption 입니다.")

# import streamlit as st

# st.title("Streamlit 소개")
# st.header("Streamlit이란?")
# st.subheader("개요")
# st.caption("Streamlit은 데이터 과학자와 머신러닝 엔지니어가 간단한 Python" 
#         "스크립트를 사용하여 대화형 웹 애플리케이션을 "
#         " 만들 수 있도록 도와주는 오픈 소스 프레임워크입니다."
#         "이를 통해 사용자는 데이터 분석, 시각회, 모델 배포 등을 빠르게 구현할 수 있습니다."
#         )
# st.subheader("주요 기능")
# st.text("Streamlit은 다음과 같은 주요 기능을 제공합니다.")
# st.markdown("- **빠른개발** : 몇 줄의 코드만으로 데이터 앱을 개발 가능")
# st.markdown("- **자동화된 UI 생성** : 코드에 따라 자동으로 웹 인터페이스가 생성됩니다.")
# st.markdown("- **실시간 업데이트** : 코드 수정 후 즉시 결과 확인 가능합니다.")
# st.markdown("- **확장성** : 다양한 차트를 지원하여 데이터 시각화에 용이합니다.")

# st.code : 코드 블록 생성
# import streamlit as st

# str = """def text():
#     print('Hello, Streamlit')
#      """
# st.code(str, language='python',  line_numbers=True) # line numbers : 라인 번호 표시

# st.title("ㅇㅇ")
# st.divider() # 구분선
# st.header("ㅇㅇ")