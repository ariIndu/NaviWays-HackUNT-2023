import streamlit as st
from constants import *
# from 01_Location import collegeStr
# location = __import__('01_Location')

color1 = "#ff9f1c"
color2 = "#2EC4B6"

collegeString = st.session_state['college_name']

background_css = """
    <style>
        body {
            background-color: #e5e5f7;
            opacity: 0.95;
            background-image: repeating-radial-gradient(circle at 0 0, transparent 0, #e5e5f7 50px), repeating-linear-gradient(#444cf755, #444cf7);
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
    </style>
"""

st.markdown(background_css, unsafe_allow_html=True)

def blank(num=1):
  for _i in range(0,num):
    st.write("\n")

def colorMD(htmlType, color, content):
  return f"<{htmlType} style='color:{color}'>{content}</{htmlType}>"

def markdown(md):
  st.markdown(md, unsafe_allow_html=True)

st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="collapsed",
)

markdown(colorMD("h1", color1,f"College: {collegeString}"))


def text_output():

    col1, col2, col3 = st.columns(3)

    col1.subheader('Academic Programs')
    col1.code('''
Academic Programs Offered
Overall Academic Reputation
Rankings
Faculty Credentials
    ''')

    col1.subheader('Campus Culture and Environment')
    col1.code('''
Campus culture
Size
student body diversity
social and extracurricular activities
lifestyle
    ''')

    col2.subheader('Financials')
    col2.code('''
Tuition
Fees and other
Financial aid
Scholarships
Work-study opportunities
graduate earning power
''')


    col2.subheader('Resources and Facilities')
    col2.code('''
Facilities
 - libraries
 - laboratories
 - technology
- recreational facilities
internships
research opportunities
''')



    col3.subheader('Networking and Alumni')
    col3.code('''
alumni success stories
graduates achievements
alumni network strength
''')

   

text_output()