import streamlit as st
import time

st.set_page_config(page_title="Instagram Profile Analyzer", layout="centered")

st.title("📊 Instagram Profile Analyzer")
st.write("Analyze **public information** of any Instagram profile")

username = st.text_input("Instagram Username")

if st.button("Analyze Profile"):
    if username.strip() == "":
        st.warning("Please enter a username")
    else:
        with st.spinner("Analyzing profile..."):
            time.sleep(2)  # simulate real processing

        # ---- DEMO / SIMULATION OUTPUT ----
        st.success("Profile analyzed successfully ✅")

        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg",
            width=150
        )

        st.write("**Username:**", username)
        st.write("**Bio:** Public Instagram user")
        st.write("**Followers:** 12,340")
        st.write("**Following:** 530")
        st.write("**Account Type:** Public 🌍")

        st.info(
            "ℹ️ Note: Due to Instagram security & rate limits, "
            "this project demonstrates analysis using a **safe simulation model**."
        )
