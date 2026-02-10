import streamlit as st
import instaloader

st.set_page_config(page_title="Instagram Profile Analyzer", layout="centered")

st.title("📊 Instagram Profile Analyzer")
st.write("Enter any Instagram username (public or private)")

username = st.text_input("Instagram Username")

if st.button("Analyze Profile"):
    if username.strip() == "":
        st.warning("Please enter a username")
    else:
        try:
            L = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(L.context, username)

            st.success("Profile Found ✅")

            st.image(profile.profile_pic_url, width=150)

            st.write("**Username:**", profile.username)
            st.write("**Bio:**", profile.biography)
            st.write("**Followers:**", profile.followers)
            st.write("**Following:**", profile.followees)
            st.write(
                "**Account Type:**",
                "Private 🔒" if profile.is_private else "Public 🌍"
            )

            if not profile.is_private:
                st.write("**Full Name:**", profile.full_name)
                st.write("**Total Posts:**", profile.mediacount)
            else:
                st.info("🔒 Private account – limited public info shown")

        except:
            st.error("Profile not found or request blocked ❌")
