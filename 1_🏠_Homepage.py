from typing import Container
import requests
import streamlit as st
from streamlit_lottie import st_lottie



# Ideas hacer el bucle para los videos
# Falta relacionar el resto de certificados
# Falta hacer enlace para trabajos en Excel
# Falta enlace para sereing sas, y enlace familiar Laura
# Falta trabajos en los cuales me he desempeñad Resumen
# Falta volver activar projectos que habia realizado como el de transmilenio




# st.set_page_config(
#     page_title="🤖Camilo franco",
#     page_icon="🐺",
#     layout='wide'

# )

st.set_page_config(
   page_title="🤖 Camilo Franco",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)




def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

Lottie_coding=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_iv4dsx3q.json")
#Lottie_coding=load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_zrqthn6o.json")

#https://lottiefiles.com/search?q=developer&category=animations&animations-page=1&style=icon
#https://www.webfx.com/tools/emoji-cheat-sheet/
st.sidebar.success(":point_up_2:choose an option!")
pdfFileObj = open('pages/Curriculum_vitae.pdf', 'rb')
st.sidebar.download_button('Download resume C.V',pdfFileObj,file_name='Curriculum_vitae.pdf',mime='pdf')


with st.container():

    left_column,right_column= st.columns([3,1],gap='small')

    with left_column:
        st.subheader("Hi,I am Camilo Franco :wave:")
        st.title('🤖Colombian Data Scientst ')
        st.write('Economist with a passion for data science. My favorite programming language is Python. \
        I am currently advancing a specialization in statistics to be able to build better machine learning and artificial intelligence models.')
        #st.write("[You can visit my git hub repository](https://github.com/camigenius)")
        st.image("pages/github.png")
        st.write("I developed this application in python language, you can visit my repository on GitHub \
        by clicking on the following link: https://github.com/camigenius")
        
        st.markdown('Visit my linkedin :https://www.linkedin.com/in/camilofrancog/')
        

    with right_column:
        st.image("pages/foto_camilo_aws.jpg",caption='AWS summit Bogota,Colombia') 


with st.container():

    st.write('---')
    column1,column2,column3= st.columns([2,3,3],gap='small')
    
    with column1:
        
        
        st.subheader(':muscle:Skills')
        #st.write('##')
        st.write(
            """
            I have knowledge in:
            - Power bi.
            - SQL.
            - Advance Excel
            - Git and Github Repository.
            - Currently learning:
                - Framework flask.
                - Fast Api.
                - Air Flow.                                 
            """
        )

    with column2:
        st.subheader('💻 Programming Languaje')
        st.write(
            """
            - Python.
                - Numpy ,Pandas
                - Matplotlib,Seaborn,Plotly,Dash.
                - StatsModels ,scikit-lern,Keras,PyTorh Others.
                - Streamlit (Deployment of machinme learning models).
                
            - Visual Basic for Application Excel VBA.
            - Bash.
            - R (statistic)            
            
            """

        )        
    
    with column3:
        
        
        st_lottie(Lottie_coding,height=280,key='coding')

with st.container():

    st.write('---')


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




# Col1,Col2=st.columns([3,4],gap='small')


# with Col1:
    
#     st.header('Python')
#     st.image("pages/foto_camilo.jpg")

# with Col2:
   
# #    st.markdown("")
# #    st.markdown("")
# #    st.markdown("")
# #    st.markdown("")
# #    st.markdown("")
# #    st.markdown("")
# #    st.markdown("")


#    st.header("Python")
#    st.image("pages/streamlit_cl_old.png")

    
# with Col3:
#     st.header("Un perro")
#     st.image("pages/streamlit_cl_old.png")




#from code.shared_functions import skip_echo

#def display():
    #_, c1, c2, _ = st.columns([2,7,3,2])
    #with c1:
# repo_path = "https://raw.githubusercontent.com/sebastiandres/talk_2021_11_pyconcl/main/images"
# st.markdown("#### PyCon: 2020 (🇨🇴, 🇦🇷) y 2021 (🌎, 🇦🇷, 🇨🇱)")
# st.markdown("# WebApps con Streamlit:")
# st.markdown("#    _¡más fácil que la tabla del uno, poh!_")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("## Sebastián Flores, Noviembre 2021")
# st.markdown("##### Presentación realizada en streamlit (:exploding_head: *streamlit-ception*)")
# st.write("Repositorio de la presentación: https://github.com/sebastiandres/talk_2021_11_pyconcl")

#     #with c2:
# st.image("pages/streamlit_cl_old.png")
