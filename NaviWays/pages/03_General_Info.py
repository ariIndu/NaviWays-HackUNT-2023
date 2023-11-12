import streamlit as st
from constants import *

color1 = "#ff9f1c"
color2 = "#2EC4B6"

cityString = st.session_state['city']



def blank(num=1):
  for _i in range(0,num):
    st.write("\n")

def colorMD(htmlType, color, content):
  return f"<{htmlType} style='color:{color}'>{content}</{htmlType}>"

def markdown(md):
  st.markdown(md, unsafe_allow_html=True)

st.set_page_config(
     # page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="collapsed",
)

markdown(colorMD("h1", color1,f"City: {cityString}"))

# def text_output_weather():

    
  
# text_output_weather()

def text_output():

    col1, col2, col3 = st.columns(3)

    col1.subheader('Weather')
    col1.code('''
  Temperature
  Precipitation
  Sun Status
  Humidity
      ''')
  
    col1.subheader('Demographics')
    col1.code('''
General Population
Male to Female Ratio
Population per Square Mile
    ''')

    col1.subheader('Economics')
    col1.code('''
Employment Rate
Average Income
Average Housing Price

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