import streamlit as st
from PIL import Image


# ------- 사이드바 화면
st.sidebar.title('사이드바')
st.sidebar.header('텍스트 입력')
user_id = st.sidebar.text_input('ID입력:', value='streamlit', max_chars=15) # 사이드 바 안에 input='text' 추가
user_pw = st.sidebar.text_input('PW입력:', value='1234', type='password')

st.sidebar.header('셀렉트 박스')
sel_opt = ['진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정인']
user_opt = st.sidebar.selectbox('좋아하는 작품은?', sel_opt) # user가 선택한 글자
st.sidebar.write('선택한 작품은:', user_opt)


# ------- 메인
st.title('스트림릿의 사이드바')
folder = 'D:/vsCode_workspace/data/'
image_files = ['Vermeer.png', 'Gogh.png', 'Munch.png', 'ShinYoonbok.png'] # 인덱스 0부터 시작

sel_img_index = sel_opt.index(user_opt) # 내가 선택한 그림의 인덱스를 가져옴
# sel_opt = ['진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정인']

st.write(sel_img_index) # 선택한 항목에 맞는 이미지 파일 저장

img_file = image_files[sel_img_index]
img_local =Image.open(folder + img_file) # PIL 이미지 열기
st.image(img_local, caption=user_opt) # 이미지 표시