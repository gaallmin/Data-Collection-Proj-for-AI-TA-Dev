import streamlit as st
from PIL import Image
import mysql.connector

st.set_page_config(
    page_title = "survey page_4",
    page_icon = ":page_with_curl:"
)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd="0000"
)

mycursor = db.cursor()
mycursor.execute("USE maininfo")
#mycursor.execute("CREATE TABLE emergency(PERSONAL_ID INT, FOREIGN KEY(PERSONAL_ID) REFERENCES info(PERSONAL_ID), Q_1 VARCHAR(5), Q_2 VARCHAR(5),Q_3 VARCHAR(5), Q_4 VARCHAR(5), Q_5_1 VARCHAR(5),Q_5_2 VARCHAR(5),Q_5_3 VARCHAR(5),Q_5_4 VARCHAR(5))")
#mycursor.execute("DROP TABLE emergency")

st.write("Hi,",st.session_state["name"])
st.title("Who should I take with?")
st.subheader("Direction: Please select one answer for each question which is close from what you think")
st.write("---")

class pic_question:
    def __init__(q,num,pic):
        q.num = num
        q.pic = pic
    def question(q):
        with st.form(f"{q.num}"):
            st.subheader(f"{q.num}.")
            st.write("상황과 문항을 천천히 읽고 가장 먼저 데려 나갈 학생을 택해주세요.")
            if q.pic != None:
                image = Image.open(f'er_{q.pic}.jpg')
                st.image(image)
            check_1 = st.checkbox("학생 A: 폐렴을 앓고 있고 체력평가에서 가장 안 좋은 결과를 받음 ",key = f"{q.num}_1")
            check_2 = st.checkbox("학생 B: 오른 다리에 깁스를 하고 있음",key = f"{q.num}_2")
            check_3 = st.checkbox("학생 C: 신체적 장애로 인해 휠체어에 앉아 있음",key = f"{q.num}_3")
            check_4 = st.checkbox("학생 D: 공포에 대한 패닉으로 움직일 수 없음",key = f"{q.num}_4")
            
            if check_1 and check_2 and check_3 and check_4 :
                st.warning("submit one answer")
            submitted = st.form_submit_button("submit")
            if submitted:
                if check_1 == True:
                    response = "A"
                if check_2 == True:
                    response = "B"
                if check_3 == True:
                    response = "C"
                if check_4 == True:
                    response ="D"
                
                return(response)


st.subheader("1-4")
st.write("당신은 2층 교실 안에 있는 선생님입니다. 갑작스런 큰 화재 발생으로 인해 반에 남아있는 학생들을 대피시켜야 할 상황이 되었습니다. 교실에도 불길이 옮겨져 1분 1초가 급박한 상황에, 당신의 도움을 필요로 하는 학생들이 네 명 존재합니다. 엘리베이터도 사용할 수 없고 다른 학생들의 도움을 받을 수도 없는 상황이라면, 다음의 네 학생 중 당신은 가장 먼저 누구를 데려 나갈 것인가요? 대피 후 다시 교실로 돌아와 다른 학생들의 구조를 도와줄 수 있는 가능성은 매우 낮습니다. (*체력평가는 근력 및 체력 상태 모두를 포함하며, 성별은 모두 같습니다. 선택지에서 언급된 요인 외의 것들은 모두 평균으로 가정합니다.)")
st.write("---")

q1 = pic_question(1,None)
answer1 = q1.question()
if answer1 == "A":
    mycursor.execute("INSERT INTO emergency(Q_1) VALUES ('A')")
if answer1 =="B":
    mycursor.execute("INSERT INTO emergency(Q_1) VALUES ('B')")
if answer1 == "C":
    mycursor.execute("INSERT INTO emergency(Q_1) VALUES ('C')")
if answer1 == "D":
    mycursor.execute("INSERT INTO emergency(Q_1) VALUES ('D')")
if answer1:
    st.success("Data saved, please go to the next question.", icon="✅")

q2 = pic_question(2,1)
answer2 = q2.question()
if answer2 == "A":
    mycursor.execute("INSERT INTO emergency(Q_2) VALUES ('A')")
if answer2 =="B":
    mycursor.execute("INSERT INTO emergency(Q_2) VALUES ('B')")
if answer2 == "C":
    mycursor.execute("INSERT INTO emergency(Q_2) VALUES ('C')")
if answer2 == "D":
    mycursor.execute("INSERT INTO emergency(Q_2) VALUES ('D')")
if answer2:
    st.success("Data saved, please go to the next question.", icon="✅")

q3 = pic_question(3,2)
answer3 = q3.question()
if answer3 == "A":
    mycursor.execute("INSERT INTO emergency(Q_3) VALUES ('A')")
if answer3 =="B":
    mycursor.execute("INSERT INTO emergency(Q_3) VALUES ('B')")
if answer3 == "C":
    mycursor.execute("INSERT INTO emergency(Q_3) VALUES ('C')")
if answer3 == "D":
    mycursor.execute("INSERT INTO emergency(Q_3) VALUES ('D')")
if answer3:
    st.success("Data saved, please go to the next question.", icon="✅")

q4 = pic_question(4,3)
answer4 = q4.question()
if answer4 == "A":
    mycursor.execute("INSERT INTO emergency(Q_4) VALUES ('A')")
if answer4 =="B":
    mycursor.execute("INSERT INTO emergency(Q_4) VALUES ('B')")
if answer4 == "C":
    mycursor.execute("INSERT INTO emergency(Q_4) VALUES ('C')")
if answer4 == "D":
    mycursor.execute("INSERT INTO emergency(Q_4) VALUES ('D')")
if answer4:
    st.success("Data saved, please go to the next question.", icon="✅")
 

with st.form("5"):
    st.subheader("5")
    st.write("당신은 한 학급의 담임으로, 학교에서 수학여행을 갔습니다. 산을 등반하던 중 인솔하던 학생이 몇 명 사라져 홀로 학생들을 찾아보니 네 명의 학생이 발을 헛디뎌 굴러 떨어져 모두 다리 부상을 입고 올라오고 있지 못하고 있었습니다. 구조대를 부를 수는 없는 상황이고, 학생들이 모여 있는 곳은 지반이 언제 무너져도 이상하지 않아 보입니다. 다행히도 당신은 밧줄을 비롯한 몇 구조 용품을 가지고 있습니다. 그러나 이미 해는 지고 기온도 낮은 상황 속에서 넷 모두 구한다 해도 더 늦게 구조 된 학생들의 안전을 보장할 수는 없으며, 당신 혼자서 넷 모두를 구조할 수 있을지 그 가능성도 희미합니다. 이런 상황 속에서 당신은 어떤 순서로 학생들을 구하겠습니까?(*체력평가는 근력 및 체력 상태 모두를 포함하며, 성별은 모두 같습니다.)")

    st.write("🤢학생 A: 폐렴을 앓고 있고 체력평가에서 가장 안 좋은 결과를 받음")
    st.write("🦿학생 B: 오른 다리에 깁스를 하고 있음")
    st.write("👨‍🦽학생 C: 신체적 장애로 인해 휠체어에 앉아 있음")
    st.write("😨학생 D: 공포에 대한 패닉으로 움직일 수 없게 됨")
    
    first = st.selectbox(
            "1️⃣->첫 번째로 구할 학생을 골라주세요",
            ('학생 A','학생 B','학생 C','학생 D')
            )

    second = st.selectbox(
        "2️⃣->두 번째로 구할 학생을  골라주세요",
        ('학생 A','학생 B','학생 C','학생 D')
        )

    third = st.selectbox(
        "3️⃣->세 번째로 구할 학생을  골라주세요",
        ('학생 A','학생 B','학생 C','학생 D')
        )

    foruth = st.selectbox(
        "4️⃣->네 번째로 구할 학생을  골라주세요",
        ('학생 A','학생 B','학생 C','학생 D')
        )

    submitted5 = st.form_submit_button("submit")
    if submitted5:
        A = '학생 A'
        B = '학생 B'
        C = '학생 C'
        D = '학생 D'

        if first == A:
            mycursor.execute("INSERT INTO (Q_5_1) VALUES ('A')")
        if first == B:
            mycursor.execute("INSERT INTO thief(Q_5_1) VALUES ('B')")
        if first == C:
            mycursor.execute("INSERT INTO thief(Q_5_1) VALUES ('C')")
        if first == D:
            mycursor.execute("INSERT INTO thief(Q_5_1) VALUES ('D')")

        if second == A:
            mycursor.execute("INSERT INTO (Q_5_2) VALUES ('A')")
        if second == B:
            mycursor.execute("INSERT INTO thief(Q_5_2) VALUES ('B')")
        if second == C:
            mycursor.execute("INSERT INTO thief(Q_5_2) VALUES ('C')")
        if second == D:
            mycursor.execute("INSERT INTO thief(Q_5_2) VALUES ('D')")

        if third == A:
            mycursor.execute("INSERT INTO (Q_5_3) VALUES ('A')")
        if third == B:
            mycursor.execute("INSERT INTO thief(Q_5_3) VALUES ('B')")
        if third == C:
            mycursor.execute("INSERT INTO thief(Q_5_3) VALUES ('C')")
        if third == D:
            mycursor.execute("INSERT INTO thief(Q_5_3) VALUES ('D')")

        if foruth == A:
            mycursor.execute("INSERT INTO (Q_5_4) VALUES ('A')")
        if foruth == B:
            mycursor.execute("INSERT INTO thief(Q_5_4) VALUES ('B')")
        if foruth == C:
            mycursor.execute("INSERT INTO thief(Q_5_4) VALUES ('C')")
        if foruth == D:
            mycursor.execute("INSERT INTO thief(Q_5_4) VALUES ('D')")


    
    st.success("Data saved, THANK YOU FOR ANSWERING❤❤", icon="✅")

