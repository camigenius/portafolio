import streamlit as st

st.set_page_config(
    page_title="Contac : Camilo franco",
    page_icon=":rocket:",
    layout='wide'
)



st.write('- "Visit my website and find consulting and learning services in Microsoft Excel and data analysis." [Click hear 📍](https://excelfriend.wixsite.com/excelfriend/services)')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


st.header(":mailbox:Get in Touch With me!")

contact_form = """
    <form action="https://formsubmit.co/camilofinanzas@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here!" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

left_column, right_column = st.columns(2)

with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()
