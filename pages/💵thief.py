import streamlit as st
from PIL import Image
import mysql.connector

st.set_page_config(
    page_title = "survey page_3",
    page_icon = ":page_with_curl:"
)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd="0000"
)

mycursor = db.cursor()
mycursor.execute("USE maininfo")
#mycursor.execute("CREATE TABLE thief(PERSONAL_ID INT, FOREIGN KEY(PERSONAL_ID) REFERENCES info(PERSONAL_ID), Q1 VARCHAR(5), Q2 VARCHAR(5),Q3 VARCHAR(5), Q4 VARCHAR(5), Q5 VARCHAR(5), Q6 VARCHAR(5), Q7 VARCHAR(5), Q8 VARCHAR(5), Q9 VARCHAR(5), Q10_1 VARCHAR(100),Q10_2 VARCHAR(100),Q10_3 VARCHAR(100),Q10_4 VARCHAR(100))")


st.write("Hi,",st.session_state["name"])

st.title("Should I report?")
st.subheader("Direction: Please select one answer for each question which is close from what you think")
st.subheader(":disappointed_relieved:")
st.write("아무도 없는 체육시간 학생 A는 다른 학생의 개인 돈을 훔쳤다. 우연한 계기로 나만 A가 범인인지를 알게 되었고 나는 현재 이 사실을 담임 선생님께 말해야 할지 고민하고 있다. 각 상황을 고려하여 자신의 선택을 골라주세요.")
st.write("")
st.write(":arrow_right:","고려 상황: 가해 학생의 가정형편, 피해 학생의 가정형편, 훔친 금액, 교사의 성향")
col1,col2 = st.columns(2)
with col1, col2:
    with col1:
        st.write(":white_check_mark:","A 성향의 교사가 사실을 알게 된다면 다음날 담임교사는 학생의 도둑질 사실을 학급 학생 모두의 앞에서 비난하고, 학생은 도둑으로 소문날 것이다")
    with col2:
        st.write(":white_check_mark:","B 성향의 교사가 사실을 알게 된다면 다음날 담임교사는 개인적으로 학생의 잘못을 타이르고, 개인 면담을 통해 문제를 해결하고자 할 것이다. ")
st.markdown("---")

class report:
    def __init__(r,num, offender, victim, amount, teach):
        r.number = num
        r.offender = offender
        r.victim = victim
        r.amount = amount
        r.teach = teach
    def title(r):
        st.subheader(f'{r.number}.')
    def cir(r):
        image = Image.open(f't_{r.number}.PNG')
        st.image(image)
        if r.offender and r.victim and r.amount != None:
            expander = st.expander("상세 설명 보기")
            expander.write(f"""
            ▪ 돈을 훔친 학생의 집안은 {r.offender}한 편이다. \n 
            ▪ 피해 학생의 집안은 {r.victim}한 편이다 \n 
            ▪ 훔친 금액은 {r.amount}이다 \n
            ▪ 이 반의 담임교사는 {r.teach} 성향을 가지고 있다.
            """)
        

    def teacher(r):
        st.caption("A 성향의 교사:평소 배려심이 부족하고 학생들의 잘못을 대놓고 혼내는 성향")
        st.caption("B 성향의 교사:평소 배려심이 많고 학생들의 잘못을 개인적으로 타이르는 성향")
    def answer(r):
        check_1 = st.checkbox("알린다",key = f"{r.number}_1")
        check_2 = st.checkbox("알리지 않는다", key = f"{r.number}_2")
        if check_1 and check_2:
            st.warning("submit one answer")

with st.form("1"):
    q1 = report(1,None,None,None,"A")
    q1.title()
    q1.teacher()
    answer_1 = q1.answer()
    submitted1 = st.form_submit_button("submit")
    if submitted1:
        if answer_1 == "O":
            mycursor.execute("INSERT INTO thief(Q1) VALUES ('O')")
        if answer_1 == "X":
            mycursor.execute("INSERT INTO thief(Q1) VALUES ('X')")   
        st.success("Data saved, please go to the next question.", icon="✅")

with st.form("2"):
    q2 = report(2,None,None,None,"B")
    q2.title()
    q2.teacher()
    answer_2 = q2.answer()
    submitted2 = st.form_submit_button("submit")
    if submitted2:
        if answer_2 == "O":
            mycursor.execute("INSERT INTO thief(Q2) VALUES ('O')")
        if answer_2 == "X":
            mycursor.execute("INSERT INTO thiefn(Q2) VALUES ('X')")
        st.success("Data saved, please go to the next question.", icon="✅")

with st.form("3"):
    q3 = report(3,"부유","가난",50000,"A")
    q3.title()
    q3.cir()
    q3.teacher()
    answer_3 = q3.answer()
    submitted3 = st.form_submit_button("submit")
    if submitted3:
        if answer_3 == "O":
            mycursor.execute("INSERT INTO thief(Q3) VALUES ('O')")
        if answer_3 == "X":
            mycursor.execute("INSERT INTO thief(Q3) VALUES ('X')")
        st.success("Data saved, please go to the next question.", icon="✅")

with st.form("4"):
    q4 = report(4,"가난","부유",5000,"A")
    q4.title()
    q4.cir()
    q4.teacher()
    answer_4 = q4.answer()
    submitted4 = st.form_submit_button("submit")
    if submitted4:
        if answer_4 == "O":
            mycursor.execute("INSERT INTO thief(Q4) VALUES ('O')")
        if answer_4 == "X":
            mycursor.execute("INSERT INTO thief(Q4) VALUES ('X')")
        st.success("Data saved, please go to the next question.", icon="✅")


with st.form("5"):
    q5 = report(5,"부유","부유",50000,"B")
    q5.title()
    q5.cir()
    q5.teacher()
    answer_5 = q5.answer()
    submitted5 = st.form_submit_button("submit")
    if submitted5:
        if answer_5 == "O":
            mycursor.execute("INSERT INTO thief(Q5) VALUES ('O')")
        if answer_5 == "X":
            mycursor.execute("INSERT INTO thief(Q5) VALUES ('X')")
        st.success("Data saved, please go to the next question.", icon="✅")


with st.form("6"):
    q6 = report(6,"부유","부유",50000,"B")
    q6.title()
    q6.cir()
    q6.teacher()
    answer_6 = q6.answer()
    submitted6 = st.form_submit_button("submit")
    if submitted6:
        if answer_6 == "O":
            mycursor.execute("INSERT INTO thief(Q6) VALUES ('O')")
        if answer_6 == "X":
            mycursor.execute("INSERT INTO thief(Q6) VALUES ('X')")
        st.success("Data saved, please go to the next question.", icon="✅")


with st.form("7"):
    q7 = report(7,"가난","부유",50000,"A")
    q7.title()
    q7.cir()
    q7.teacher()
    answer_7 = q7.answer()
    submitted7 = st.form_submit_button("submit")
    if submitted7:
        if answer_7 == "O":
            mycursor.execute("INSERT INTO thief(Q7) VALUES ('O')")
        if answer_7 == "X":
            mycursor.execute("INSERT INTO thief(Q7) VALUES ('X')")
        st.success("Data saved, please go to the next question.", icon="✅")


with st.form("8"):
    q8 = report(8,"부유","가난",50000,"B")
    q8.title()
    q8.cir()
    q8.teacher()
    answer_8 = q8.answer()
    submitted8 = st.form_submit_button("submit")
    if submitted8:
        if answer_8 == "O":
            mycursor.execute("INSERT INTO thief(Q8) VALUES ('O')")
        if answer_8 == "X":
            mycursor.execute("INSERT INTO thief(Q8) VALUES ('X')")
        st.success("Data saved, please go to the next question.", icon="✅")


with st.form("9"):
    q9 = report(9,"가난","부유",5000,"B")
    q9.title()
    q9.cir()
    q9.teacher()
    answer_9 = q9.answer()
    submitted9 = st.form_submit_button("submit")
    if submitted9:
        if answer_9 == "O":
            mycursor.execute("INSERT INTO thief(Q9) VALUES ('O')")
        if answer_9 == "X":
            mycursor.execute("INSERT INTO thief(Q9) VALUES ('X')")
        st.success("Data saved, please go to the next question.", icon="✅")

# mycursor.execute("ALTER TABLE theif ADD Q_10_2 VARCHAR(10)")
#mycursor.execute("ALTER TABLE theif ADD Q_10_3 VARCHAR(10)")
#mycursor.execute("ALTER TABLE theif ADD Q_10_4 VARCHAR(10)")

with st.form("10"):
    st.subheader("10")
    st.write("앞선 문항들에 대한 자신이 중요하게 고려한 요소는 무엇입니까?")
    first = st.selectbox(
        "1️⃣->첫 번째로 중요했던 요소를 골라주세요",
        ('가해 학생의 가정형편','피해 학생의 가정형편','훔친 금액','조치 후 상황(담임 선생님의 성향)')
        )

    second = st.selectbox(
        "2️⃣->두 번째로 중요했던 요소를 골라주세요",
        ('피해 학생의 가정형편','가해 학생의 가정형편','훔친 금액','조치 후 상황(담임 선생님의 성향)')
        )

    third = st.selectbox(
        "3️⃣->세 번째로 중요했던 요소를 골라주세요",
        ('훔친 금액','가해 학생의 가정형편','피해 학생의 가정형편','조치 후 상황(담임 선생님의 성향)')
        )

    foruth = st.selectbox(
        "4️⃣->네 번째로 중요했던 요소를 골라주세요",
        ('조치 후 상황(담임 선생님의 성향)','가해 학생의 가정형편','피해 학생의 가정형편','훔친 금액')
        )
  
    submitted10 = st.form_submit_button("submit")
    if submitted10:
        A = '가해 학생의 가정형편'
        B = '피해 학생의 가정형편'
        C = '훔친 금액'
        D = '조치 후 상황(담임 선생님의 성향)'

        if first == A:
            mycursor.execute("INSERT INTO thief(Q10_1) VALUES ('가해 학생의 가정형편')")
        elif first == B:
            mycursor.execute("INSERT INTO thief(Q10_1) VALUES ('피해 학생의 가정형편')")
        elif first == C:
            mycursor.execute("INSERT INTO thief(Q10_1) VALUES ('훔친 금액')")
        elif first == D:
            mycursor.execute("INSERT INTO thief(Q10_1) VALUES ('조치 후 상황(담임 선생님의 성향)')")

        if second == A:
            mycursor.execute("INSERT INTO thief(Q10_2) VALUES ('가해 학생의 가정형편')")
        elif second == B:
            mycursor.execute("INSERT INTO thief(Q10_2) VALUES ('피해 학생의 가정형편')")
        elif second == C:
            mycursor.execute("INSERT INTO thief(Q10_2) VALUES ('훔친 금액')")
        elif second == D:
            mycursor.execute("INSERT INTO thief(Q10_2) VALUES ('조치 후 상황(담임 선생님의 성향)')")

        if third == A:
            mycursor.execute("INSERT INTO thief(Q10_3) VALUES ('가해 학생의 가정형편')")
        elif third == B:
            mycursor.execute("INSERT INTO thief(Q10_3) VALUES ('피해 학생의 가정형편')")
        elif third == C:
            mycursor.execute("INSERT INTO thief(Q10_3) VALUES ('훔친 금액')")
        elif third == D:
            mycursor.execute("INSERT INTO thief(Q10_3) VALUES ('조치 후 상황(담임 선생님의 성향)')")

        if foruth == A:
            mycursor.execute("INSERT INTO thief(Q10_4) VALUES ('가해 학생의 가정형편')")
        elif foruth == B:
            mycursor.execute("INSERT INTO thief(Q10_4) VALUES ('피해 학생의 가정형편')")
        elif foruth == C:
            mycursor.execute("INSERT INTO thief(Q10_4) VALUES ('훔친 금액')")
        elif foruth == D:
            mycursor.execute("INSERT INTO thief(Q10_4) VALUES ('조치 후 상황(담임 선생님의 성향)')")
       
        st.success("Data saved, please go to the section 'placement'.", icon="✅")