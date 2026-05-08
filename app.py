import streamlit as st
import google.generativeai as genai

# إعداد واجهة المستخدم بأسلوب مظلم وعصري
st.set_page_config(page_title="الذكاء الخاص بي V01.0", layout="centered")

st.title("🤖 My Personal AI V01.0")
st.markdown("---")

# إدخال مفتاح الـ API (يمكنك الحصول عليه مجاناً من Google AI Studio)
api_key = st.sidebar.text_input("ادخل API Key الخاص بك:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض المحادثة
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # استقبال سؤال المستخدم
    if prompt := st.chat_input("كيف يمكنني مساعدتك اليوم؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.info("يرجى إدخال مفتاح API للبدء. يمكنك الحصول عليه مجاناً من Google AI Studio.")
