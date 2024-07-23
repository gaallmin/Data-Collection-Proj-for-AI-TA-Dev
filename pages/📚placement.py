import streamlit as st
import pandas as pd
import mysql.connector


st.set_page_config(
    page_title = "survey page_2",
    page_icon = ":page_with_curl:"
)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd="0000"
)

mycursor = db.cursor()
mycursor.execute("USE maininfo")
#mycursor.execute("CREATE TABLE placement(PERSONAL_ID INT, FOREIGN KEY(PERSONAL_ID) REFERENCES info(PERSONAL_ID), Q1 VARCHAR(5), Q2 VARCHAR(5),Q3 VARCHAR(5), Q4 VARCHAR(5), Q5 VARCHAR(5), Q6 VARCHAR(5), Q7 VARCHAR(5), Q8 VARCHAR(5), Q9 VARCHAR(5), Q10 VARCHAR(5), Q11 VARCHAR(5), Q12 VARCHAR(5))")
#mycursor.execute("DROP TABLE placement")
#mycursor.execute("CREATE TABLE placement(PERSONAL_ID INT, FOREIGN KEY(PERSONAL_ID) REFERENCES info(PERSONAL_ID), Q1 VARCHAR(5), Q2 VARCHAR(10),Q3 VARCHAR(5), Q4 VARCHAR(5), Q5 VARCHAR(5), Q6 VARCHAR(5), Q7 VARCHAR(5), Q8 VARCHAR(5), Q9 VARCHAR(5), Q10 VARCHAR(5), Q11 VARCHAR(5), Q12 VARCHAR(5))")

st.header("Hi,",st.session_state["name"])



st.title(":thumbsup:")
st.title("What is the perfect placement?")
st.subheader("Direction: Please select one answer for each question which is close from what you think")

st.markdown("---")
with st.form("1-1"):
    st.subheader("1.")
    st.write("당신은 현재 2학년 학생들의 학년 진급을 앞두고 선택과목 반을 편성하고 있습니다. 선택과목은 사전의 설문조사를 통해 학생들의 1지망과 2지망을 파악하여 성적순으로 반을 배정하고 있습니다. 그러던 도중 당신은 ‘물리Ⅱ’ 반의 한 자리만을 남겨두고 큰 고민에 빠졌습니다. 두 명의 학생이 ‘물리Ⅱ’ 반을 희망하는데 두 학생의 평균 등급이 똑같아 누구를 배정해야 할지 애매한 상황입니다. 학생 A는 물리학과에 진학하는 것이 목표며, 학생부 종합 전형을 준비해 생활기록부도 물리를 주제로 한 다양한 활동으로 가득 차있는 상태입니다. 학생 B는 평소의 관심사로 보나 생활기록부로 보나 물리 과목에 대한 특별한 애착이 있지는 않지만, ‘물리Ⅰ’ 과목을 비롯한 과학 탐구의 등급이 모두 학생 A보다 높습니다. 이런 상황에서 당신은 누구를 ‘물리Ⅱ’반에 배정할 것인가요?")
    check_1 = st.checkbox("A")
    check_2 = st.checkbox("B")
    if check_1 and check_2:
        st.warning("submit one answer")
    submitted_1 = st.form_submit_button("submit")
    if submitted_1:
        if check_1 == True:
            mycursor.execute("INSERT INTO placement(Q1) VALUES ('A')")
        if check_2 == True:
            mycursor.execute("INSERT INTO placement(Q1) VALUES ('B')")
        st.success("Data saved, please go to the next question.", icon="✅")

with st.form("1-2"):
    st.subheader("2.")
    st.write("위와 같은 상황에서 학생의 ‘흥미(생활기록부와 장래희망)’와 ‘성적(물리Ⅰ을 비롯한 과학탐구 성적)’ 중 어느 요소에 더 초점을 두고 반 배정을 해야 한다고 생각하시나요?")
    check_i = st.checkbox("흥미")
    check_h = st.checkbox("적성")
    if check_1 and check_2:
        st.warning("submit one answer")
    submitted_2 = st.form_submit_button("submit")
    
    if submitted_2:
        if check_i == True:
            mycursor.execute("INSERT INTO placement(Q2) VALUES ('흥미')")
        if check_h == True:
            mycursor.execute("INSERT INTO placement(Q2) VALUES ('적성')")
        st.success("Data saved, please go to the next question.", icon="✅")



table_interest = {
        "점수": ['10점 이하','10점 초과 30점 이하','30점 초과 50점 이하','50점 초과 70점 이하','70점 초과 90점 이하','90점 초과']
        ,"흥미 정도" : ['해당 과목에 관심이 없음','거의 흥미를 갖고 있지 않음','약간의 흥미를 갖고 있음', '높은 흥미를 갖고 있음','매우 높은 흥미를 갖고 있음','사실상 산출 불가능한 점수로, 해당 과목에 대한 애정이 확고함']
    }

with st.form("3"):
    st.subheader("3.")
    st.write("학생들의 물리에 대한 *흥미점수를 바탕으로 반 배정을 결정한다고 할 때, 물리Ⅱ 수업을 듣기 위해 학생들이 가져야 할 흥미점수에 대한 최소치를 선택해주세요. ")
    st.caption("*흥미 점수는 학생 생활기록부를 특정 기준을 적용해 점수로 환산하고 시험을 제외한 과제 점수와 합산해 수치로 나타낸 점수이며, 100점 만점입니다. 가장 높은 점수인 ‘90점 초과’는 선택항목에서 제외하고, 가장 낮은 점수인 ‘10점 이하’는 ‘반 배정과 아무런 관련이 없다’는 문항으로 대체하였습니다)")
    
    table_3 = pd.DataFrame(table_interest)
    st.table(table_3)
    check_a = st.checkbox("물리에 대한 흥미 점수는 물리Ⅱ 반 배정과 아무런 관련이 없다.")
    check_b = st.checkbox("10점 초과 30점 이하")
    check_c = st.checkbox("30점 초과 50점 이하")
    check_d = st.checkbox("50점 초과 70점 이하")
    check_e = st.checkbox("70점 초과 90점 이하")
    if check_a and check_b and check_c and check_d and check_e:
        st.warning("submit one answer")
    submitted_3 = st.form_submit_button("submit")
    if submitted_3:
        if check_a == True:
            mycursor.execute("INSERT INTO placement(Q3) VALUES ('X')")
        if check_b == True:
            mycursor.execute("INSERT INTO placement(Q3) VALUES ('10')")
        if check_c == True:
            mycursor.execute("INSERT INTO placement(Q3) VALUES ('30')")
        if check_d == True:
            mycursor.execute("INSERT INTO placement(Q3) VALUES ('50')")
        if check_e == True:
            mycursor.execute("INSERT INTO placement(Q3) VALUES ('70')")
        st.success("Data saved, please go to the next question.", icon="✅")

table_physics = {
    "등급": ['%d' % i for i in range(9)]
    ,"비율" : ['상위 4%이하','상위 4%초과 11%이하','상위 11%초과 23%이하','상위 23%초과 40%이하','상위 40%초과 60%이하','상위 60%초과 77%이하','상위 77%초과 89%이하','상위 89%초과 96%이하','상위 96%초과']
}

with st.form("4"):
    st.subheader("4.")
    st.write("학생들의 물리Ⅰ 등급을 바탕으로 반 배정을 결정한다고 할 때, 물리Ⅱ 수업을 듣기 위해 학생들이 받아야 할 등급의 최소치를 선택해주세요. (가장 높은 등급인 ‘1등급’은 선택항목에서 제외하고, 가장 낮은 등급인 ‘9등급’은 ‘반 배정과 아무런 관련이 없다’는 문항으로 대체하였습니다.)")
    
    table_4 = pd.DataFrame(table_physics)
    st.table(table_4)
    grade_1 = st.checkbox("물리Ⅰ 등급은 물리Ⅱ 반 배정과 아무런 관련이 없다.")
    grade_2 = st.checkbox("1등급")
    grade_3 = st.checkbox("2등급")
    grade_4 = st.checkbox("3등급")
    grade_5 = st.checkbox("4등급")
    grade_6 = st.checkbox("5등급")
    grade_7 = st.checkbox("6등급")
    grade_8 = st.checkbox("7등급")
    grade_9 = st.checkbox("8등급")

    if grade_1 and grade_2 and grade_3 and grade_4 and grade_5 and grade_6 and grade_7 and grade_8 and grade_9:
        st.warning("submit one answer")
    submitted_4 = st.form_submit_button("submit")
    if submitted_4:
        if grade_1 == True:
            mycursor.execute("INSERT INTO placement(Q4) VALUES ('X')")
        if grade_2 == True:
            mycursor.execute("INSERT INTO placement(Q4) VALUES ('1')")
        if grade_3 == True:
            mycursor.execute("INSERT INTO placement(Q4) VALUES ('2')")
        if grade_4 == True:
            mycursor.execute("INSERT INTO placement(Q4) VALUES ('3')")
        if grade_5 == True:
            mycursor.execute("INSERT INTO placement(Q4) VALUES ('4')")
        if grade_6 == True:
            mycursor.execute("INSERT INTO placement(Q4) VALUES ('5')")
        if grade_7 == True:
            mycursor.execute("INSERT INTO placement(Q4) VALUES ('6')")
        if grade_8 == True:
            mycursor.execute("INSERT INTO placement(Q4) VALUES ('7')")
        if grade_9 == True:
            mycursor.execute("INSERT INTO placement(Q4) VALUES ('8')")
        st.success("Data saved, please go to the next question.", icon="✅")

class complex:
    def __init__(complex, num, a_i, a_p, b_i, b_p):
        complex.num = num
        complex.a_i = a_i
        complex.a_p = a_p
        complex.b_i = b_i
        complex.b_p = b_p

    def question(complex):
        with st.form(f"{complex.num}"):
            st.write (f"{complex.num}. 학생 A의 물리에 대한 흥미점수는 {complex.a_i}, 물리Ⅰ 등급은 {complex.a_p}일 때, 학생 B의 물리에 대한 흥미점수는 {complex.b_i}, 물리Ⅰ 등급은 {complex.b_p}이다.")
            check_1 = st.checkbox("A",key = complex.num)
            check_2 = st.checkbox("B", key = complex.num + 8)
            if check_1 and check_2:
                st.warning("submit one answer")
            submitted = st.form_submit_button("submit")
            if submitted:
                if check_1 == True:
                    response = "A"
                elif check_2 == True:
                    response = "B"
                return(response)
        

st.subheader("5-12.")
st.write("학생들의 흥미 점수와 학업 점수를 종합적으로 고려하여 반을 배정하려고 합니다. 각 상황에서 A와 B 학생 중 누구를 '물리Ⅱ' 반에 배정할 지 선택해주세요.")
col1,col2 = st.columns(2)
with col1:
    table_i = pd.DataFrame(table_interest)
    st.table(table_i)
with col2:
    table_p = pd.DataFrame(table_physics)
    st.table(table_p)
        

    st.markdown("---")


q1 = complex(5,85,2,5,1)
answer1 = q1.question()
if answer1 == "A":
    mycursor.execute("INSERT INTO placement(Q5) VALUES ('A')")
if answer1 =="B":
    mycursor.execute("INSERT INTO class_selection(Q5) VALUES ('B')")
st.markdown("#")


q2 = complex(6,85,6,5,2)
answer2 = q2.question()
if answer2 == "A":
    mycursor.execute("INSERT INTO placement(Q6) VALUES ('A')")
if answer2 =="B":
    mycursor.execute("INSERT INTO class_selection(Q6) VALUES ('B')")
st.markdown("#")

q3 = complex(7,55,6,45,2)
answer3 = q3.question()
if answer3 == "A":
    mycursor.execute("INSERT INTO placement(Q7) VALUES ('A')")
if answer3 =="B":
    mycursor.execute("INSERT INTO class_selection(Q7) VALUES ('B')")
st.markdown("#")

q4 = complex(8,75,6,35,1)
answer4 = q4.question()
if answer4 == "A":
    mycursor.execute("INSERT INTO placement(Q8) VALUES ('A')")
if answer4 =="B":
    mycursor.execute("INSERT INTO class_selection(Q8) VALUES ('B')")
st.markdown("#")

q5 = complex(9,60,2,45,1)
answer5 = q5.question()
if answer5 == "A":
    mycursor.execute("INSERT INTO placement(Q9) VALUES ('A')")
if answer5 =="B":
    mycursor.execute("INSERT INTO class_selection(Q9) VALUES ('B')")
st.markdown("#")

q6 = complex(10,60,6,45,2)
answer6 = q6.question()
if answer6 == "A":
    mycursor.execute("INSERT INTO placement(Q10) VALUES ('A')")
if answer6 =="B":
    mycursor.execute("INSERT INTO class_selection(Q10) VALUES ('B')")
st.markdown("#")

q7 = complex(11,55,3,45,2)
answer7 = q7.question()
if answer7 == "A":
    mycursor.execute("INSERT INTO placement(Q11) VALUES ('A')")
if answer7 =="B":
    mycursor.execute("INSERT INTO class_selection(Q11) VALUES ('B')")
st.markdown("#")

q8 = complex(12,75,3,35,2)
answer8 = q8.question()
if answer8 == "A":
    mycursor.execute("INSERT INTO placement(Q12) VALUES ('A')")
if answer8 =="B":
    mycursor.execute("INSERT INTO class_selection(Q12) VALUES ('B')")
if answer8 == "A" or "B":
    st.success("Data saved, please go to the 'emergency' section.", icon="✅")