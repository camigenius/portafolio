import streamlit as st
import time
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Contac : Camilo franco",
    page_icon=":snake:",
    layout='wide'
)


st.title("Projects")



# import shapefile

st.empty()
my_bar = st.progress(0)
for i in range(50):
    my_bar.progress(i + 1)
    time.sleep(0.1)


n_elts = int(time.time() * 10) % 5 + 3

st.write("[Linear Regresion Model](https://camigenius-linear-regression-regresion2-ofmge6.streamlit.app/)")
st.write("[Cluster Model](https://camigenius-cluster-model-deploy-streamlit-app-edl2qu.streamlit.app/)")

for i in range(n_elts):
    st.text("." * i)
st.write(n_elts)
for i in range(n_elts):
    st.text("." * i)
st.success("done")