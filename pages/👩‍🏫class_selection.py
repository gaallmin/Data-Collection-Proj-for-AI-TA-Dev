import streamlit as st
import mysql.connector

st.set_page_config(
    page_title = "survey page_1",
    page_icon = ":page_with_curl:"
)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd="0000"
)

mycursor = db.cursor()
mycursor.execute("USE maininfo")
#mycursor.execute("CREATE TABLE class_selection(PERSONAL_ID INT, FOREIGN KEY(PERSONAL_ID) REFERENCES info(PERSONAL_ID), Q_1 VARCHAR(5), Q_2 VARCHAR(5),Q_3 VARCHAR(5))")

st.write("Hi,",st.session_state["name"])
st.title("Should I take with?")
st.subheader("Direction: Please select one answer for each question which is close from what you think")
st.write("---")
st.subheader(":speech_balloon:")
st.write("교사는 발표를 통한 수행평가를 진행하려고 한다.")
st.write("이때, 발표공포증이 있어 발표를 어려워하는 학생 A가 교사에게 대체과제를 요청했다.")
st.write("대체과제를 줄 경우, 교사는 이 학생에게 정상적인 수행평가를 하는 학생들과 어떤 차별점을 줘야할지 고민 중이다. 따라서 교사는 학생들에게 익명 투표를 통해 고민에 도움을 얻고자 한다.")
st.write("교사는 익명 투표를 기반으로 A,B,C 와 같은 3가지 방안을 생각하고 있다. 자신과 가장 유사한 생각을 골라주세요.")
st.write("---")
st.subheader(":astonished:")
st.write("A: 학생을 설득해 발표하게끔 한다.")
st.write("B: 학생에게 대체과제를 주되, 정상적인 방법으로 수행평가에 참여한 학생들과의 점수 차이를 어떻게 줄지는 교사가 직접 정한다.")
st.write("C: 학생에게 대체과제를 주되, 정상적인 방법으로 수행평가에 참여한 학생들과의 점수 차이를 어떻게 줘야할지는 학생들의 의견을 받는다.")
st.markdown("##")
class sel_question:
    def __init__(q,num,por):
        q.num = num
        q.por = por
    def question(q):
        with st.form(f"{q.num}"):
            st.subheader(f"{q.num}")
            st.write(f"{q.por}%의 학생이 A에게 대체과제를 주는 것에 찬성했을 경우, 당신의 대처방안을 선택하시오.")
            
            check_1 = st.checkbox("A", key = f"{q.num}_1")
            st.caption("A:학생을 설득해 발표하게끔 한다.")
            check_2 = st.checkbox("B", key = f"{q.num}_2")
            st.caption("B:학생에게 대체과제를 주되, 정상적인 방법으로 수행평가에 참여한 학생들과의 점수 차이를 어떻게 줄지는 교사가 직접 정한다.")
            check_3 = st.checkbox("C", key = f"{q.num}_3")
            st.caption("C: 학생에게 대체과제를 주되, 정상적인 방법으로 수행평가에 참여한 학생들과의 점수 차이를 어떻게 줘야할지는 학생들의 의견을 받는다.")

            if check_1 and check_2 and check_3 :
                st.warning("submit one answer")

            submitted = st.form_submit_button("submit")

            if submitted:
                if check_1 == True:
                    response = "A"
                elif check_2 == True:
                    response = "B"
                elif check_3 == True:
                    response = "C"
                
                return(response)
            

            
    

q1 = sel_question(1,10)
answer_1 = q1.question()
if answer_1 == "A":
    mycursor.execute("INSERT INTO class_selection(Q_1) VALUES ('A')")
elif answer_1 =="B":
    mycursor.execute("INSERT INTO class_selection(Q_1) VALUES ('B')")
elif answer_1 == "C":
    mycursor.execute("INSERT INTO class_selection(Q_1) VALUES ('C')")
if answer_1:
    st.success("Data saved, please go to the next question.", icon="✅")

q2 = sel_question(2,50)
answer_2 = q2.question()
if answer_2 == "A":
    mycursor.execute("INSERT INTO class_selection(Q_2) VALUES ('A')")
elif answer_2 =="B":
    mycursor.execute("INSERT INTO class_selection(Q_2) VALUES ('B')")
elif answer_2 == "C":
    mycursor.execute("INSERT INTO class_selection(Q_2) VALUES ('C')")
if answer_2:
    st.success("Data saved, please go to the next question. ", icon="✅")

q3 = sel_question(3,90)
answer_3 = q3.question()
if answer_3 == "A":
    mycursor.execute("INSERT INTO class_selection(Q_3) VALUES ('A')")
elif answer_3 =="B":
    mycursor.execute("INSERT INTO class_selection(Q_3) VALUES ('B')")
elif answer_3 == "C":
    mycursor.execute("INSERT INTO class_selection(Q_3) VALUES ('C')")
if answer_3:
    st.success("Data saved, please go to the section 'thief' ", icon="✅")


        # the answer of each question will be check_1 or 2 or 3, then how can i save the data which will be only one value
        # inside the com the check_n that is selected will the only one that has the ture value, then i have to save only the true value
        # but the problem is that the true value comes from each question
        
       