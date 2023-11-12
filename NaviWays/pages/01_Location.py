import streamlit as st
from constants import *

color1 = "#ff9f1c"
color2 = "#2EC4B6"

cityStr = ""
collegeStr = ""

st.set_page_config(initial_sidebar_state="collapsed")

# "st.session_state object:", st.session_state

def blank(num=1):
  for _i in range(0,num):
    st.write("\n")

def colorMD(htmlType, color, content):
  return f"<{htmlType} style='color:{color}'>{content}</{htmlType}>"

def markdown(md):
  st.markdown(md, unsafe_allow_html=True)
  
#   # from streamlit extras ----------------------
def switch_page(page_name: str):
  """
  Switch page programmatically in a multipage app

  Args:
      page_name (str): Target page name
  """
  from streamlit.runtime.scriptrunner import RerunData, RerunException
  from streamlit.source_util import get_pages

  def standardize_name(name: str) -> str:
      return name.lower().replace("_", " ")

  page_name = standardize_name(page_name)

  pages = get_pages("Location.py")  # OR whatever your main page is called

  for page_hash, config in pages.items():
      if standardize_name(config["page_name"]) == page_name:
          raise RerunException(
              RerunData(
                  page_script_hash=page_hash,
                  page_name=page_name,
              )
          )

  page_names = [standardize_name(config["page_name"]) for config in pages.values()]

  raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")
  
#   #----------------------
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

#--------------

#---------------



markdown(colorMD("h1","#ff9f1c","NaviWays"))

countryStr = st.selectbox(label="Country", options=["","India", "USA", "Japan"], key="country", help="Select Your Country Name")

# cityStr = st.text_input(label="City", value="" , key="city", help="Enter Your City Name")

match countryStr:
  case "India":
    cityStr = st.selectbox(label="City", options=["","Mumbai", "Hyderabad"], key="city", help="Select Your City Name")
  case "USA":
    cityStr = st.selectbox(label="City", options=["","Dallas, TX", "Austin, TX", "Tampa, FL"], key="city", help="Select Your City Name")
  case "Japan":
    cityStr = st.selectbox(label="City", options=["","Tokyo", "Fukuoka"], key="city", help="Select Your City Name")

    

check = st.checkbox ("Click to Search School")
if check:
  match cityStr:
    case "Mumbai":
      collegeStr = st.selectbox(label="School Name", options=["IIT Bombay"], key="college_name", help="Enter The Name of Your School", placeholder="Enter Your School Name")
    case "Hyderabad":
      collegeStr = st.selectbox(label="School Name", options=["","IIT Hyderabad"], key="college_name", help="Enter The Name of Your School")
    case "Dallas, TX":
      collegeStr = st.selectbox(label="School Name", options=["","UT Dallas"], key="college_name", help="Enter The Name of Your School")
    case "Austin, TX":
      collegeStr = st.selectbox(label="School Name", options=["","UT Austin"], key="college_name", help="Enter The Name of Your School")
    case "Tampa, FL":
      collegeStr = st.selectbox(label="School Name", options=["","University of South Florida"], key="college_name", help="Enter The Name of Your School")
    case "Tokyo":
      collegeStr = st.selectbox(label="School Name", options=["","University of Tokyo"], key="college_name", help="Enter The Name of Your School")
    case "Fukuoka":
      collegeStr = st.selectbox(label="School Name", options=["","Fukuoka Institute of Technology"], key="college_name", help="Enter The Name of Your School")
  
  
  if (countryStr != ""):
    if 'country' not in st.session_state:
      st.session_state['country'] = countryStr
#    st.write(f"Country: {countryStr}")
    
  if (cityStr != ""):
    if 'city' not in st.session_state:
      st.session_state['city'] = cityStr
#    st.write(f"City: {cityStr}")
    
  if (collegeStr != ""):
#    st.write(f"College: {collegeStr}")
    if 'college_name' not in st.session_state:
      st.session_state['college_name'] = collegeStr
    collegeState = st.button("Continue")
    # if collegeState("Continue"):
    #   nav_page("College")
    if collegeState:
      switch_page("College_Info")

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

if (countryStr and cityStr != ""):
  st.write("This is General_Info.")
  genInfo = st.button("Click for General Info")
  if genInfo:
    switch_page("General_Info")
    
  st.write("This is Cautions.")
  cautionsInfo = st.button("Cautions")
  if cautionsInfo:
    switch_page("Cautions")

  st.write("This is Localities.")
  localityInfo = st.button("Localities")
  if localityInfo:
    switch_page("Localities")
    
else:
  if (countryStr != ""):
    if 'country' not in st.session_state:
      st.session_state['country'] = countryStr
    st.write(f"Country: {countryStr}")
    
  if (cityStr != ""):
    if 'city' not in st.session_state:
      st.session_state['city'] = cityStr
    st.write(f"City: {cityStr}")