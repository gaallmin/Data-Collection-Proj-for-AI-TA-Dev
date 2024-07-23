import streamlit as st
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd="0000"
)

mycursor = db.cursor()
#mycursor.execute("CREATE DATABASE maininfo;")
mycursor.execute("USE maininfo;")
#mycursor.execute("CREATE TABLE info(PERSONAL_ID INT AUTO_INCREMENT PRIMARY KEY, STATUS VARCHAR(50), AGE INT)")



st.set_page_config(
    page_title = "survey main page",
    page_icon = ":page_with_curl:"
)

st.title(":wave:")
st.title("WELCOME")
st.subheader("Before the survey, please enter your information for better statics :)")
st.sidebar.success("select the section")

with st.form("basic information"):
    col1,col2 = st.columns(2)
    with grcol1:
        if "name" not in st.session_state:
            st.session_state["name"] = ""
        st.write("<Nickname>")
        name = st.text_input("input your nickname here", st.session_state["name"])
    
    with col2:
        st.write("<Status>")
        status = st.selectbox("your status", ('teacher', 'student','not in school (not a student/ teacher)'))


        st.write("<Age>")
        age = st.text_input('which age range are you in? (please write only in number')
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if status == 'teacher':
            mycursor.execute(f"INSERT INTO info(STATUS,AGE) VALUES ('teacher',{age})")
            st.success("Data saved, please go to section 'class selection' ", icon="✅")
            
        if status == 'student':
            mycursor.execute(f"INSERT INTO info(STATUS, AGE) VALUES ('student',{age})")
            st.success("Data saved, please go to section 'class selection' ", icon="✅")

        if status == 'not in school (not a student/ teacher)':
            mycursor.execute(f"INSERT INTO info(STATUS, AGE) VALUES ('NONE',{age})")
            st.success("Data saved, please go to section 'class selection' ", icon="✅")
