import streamlit as st
from PIL import Image



st.title("- [View Statistics as a teacher](https://appconnectsheet.streamlit.app/)")


# URL a la que se redirigirá
url = "https://appconnectsheet.streamlit.app/"

# Botón para redirigir a la URL especificada
if st.button("Click to see the picture"):
    image = Image.open('pages/ClasePowerbi.jpeg')
    st.image(image, caption='Class Intecap Institute')