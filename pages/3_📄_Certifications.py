from operator import contains
from typing import Container
import streamlit as st

st.set_page_config(
    page_title="Contac : Camilo franco",
    page_icon=":cat:",
    layout='wide'
)

# st.title(":trophy:knowledge")

st.title(":brain: knowledge")

with st.container():
    
    st.write('---')

    st.subheader('- University Degree')
    st.write('- Economist :Universisdad Católica de Colombia')
    st.write('- Graduate student in applied statistics: Universidad Los Libertadores')
    
with st.container():

    st.subheader('- Others')
    st.write('- Certificate in Data Science and Machine Learning :(Universidad Nacional de Colombia(🇨🇴)')
    st.write('- Certificate in Big Data (Universidad Nacional de Colombia(🇨🇴))')
    st.write('- Certificate in data analysis and visualization with python (Universidad Nacional de Colombia(🇨🇴))')
    st.write('- ([Spatial analysis of data and its applications in Python](https://wallet.xertify.co/certificates/97594132C001)(Universidad de los Andes)(🇨🇴)')
with st.container():
    st.subheader('- Courses ')
    st.write('(Notice: Click on the link to view the certificate online)')
    st.write("- [Software Engineering Fundamentals](https://platzi.com/p/camilobursatil/curso/1098-ingenieria/diploma/detalle/)")
    st.write('- [Object Oriented Programming: OOP](https://platzi.com/p/camilobursatil/curso/1474-oop/diploma/detalle/)')
    st.write('- [Introduction to Machine Learning by MindsDB](https://platzi.com/p/camilobursatil/curso/2459-machine-learning/diploma/detalle/)')
    st.write('- [Introduction to backend development](https://platzi.com/p/camilobursatil/curso/2508-introduccion-backend/diploma/detalle/)')
    st.write('- [Data Ethics and Data Management for Data Science and Artificial Intelligence](https://platzi.com/p/camilobursatil/curso/3156-etica-ia/diploma/detalle/)')
    st.write('- [Business Analytics for Data Science](https://platzi.com/p/camilobursatil/curso/2069-negocios-data-science/diploma/detalle/)')
    st.write('- [Python Intermediate: Comprehensions, Lambdas and Error Handling](https://platzi.com/p/camilobursatil/curso/2255-python-intermedio/diploma/detalle/)')
    #st.markdown("#### PyCon: 2020 (🇨🇴, 🇦🇷) y 2021 (🌎, 🇦🇷, 🇨🇱)")
    st.image("pages/github.png")



