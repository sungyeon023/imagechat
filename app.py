from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# 환경 변수 로드
load_dotenv()

# API 키 설정
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 페이지 설정
st.set_page_config(page_title="Image Chat Bot", page_icon="🗣️")

# 페이지 제목
st.header("My Image Chat Bot Web Application")

# 질문 입력
question = st.text_input("Write your question here...")

# 이미지 업로드
uploaded_image = st.file_uploader("Choose an Image..", type=["jpg", "png", "jpeg"])

# 제출 버튼
submit = st.button("Submit")

# 업로드된 이미지가 있는 경우 화면에 표시
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# 제출 버튼 클릭 시 실행
if submit:
    # 질문이 입력된 경우만 실행
    if question:
        try:
            # Generative AI 모델 사용 예시
            response = genai.generate_text(prompt=question)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
