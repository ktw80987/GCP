# import streamlit as st

# 미디어 오소
# 이미지, 오디오, 비디오 파일을 출력

# from PIL import Image # PIL : Python의 이미지 처리를 위한 라이브러리

# st.image : 이미지 출력|
# image= st.image(Image.open("image.jpeg"), width = 300) # width로 사진 크기 조절 (정사각형 형태로 조절 가능)

# st.video
# # st.video : 동영상 컨텐츠
# video = st.video("example1.mp4") # example1.mp4 파일을 출력
# video = st.video("example1.mp4", start_time = 10) # start_time으로 동영상 시작 시간 지정
# video = open("example1.mp4", "rb")
# video_bytes = video.read()
# st.video(video_bytes) # 동영상 파일을 바이트로 읽어서 출력

# url = "https://youtu.be/cCKCgs7xat4"
# st.video(url) # 유튜브 동영상 링크를 출력