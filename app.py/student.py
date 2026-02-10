import streamlit as st
import mysql.connector
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_db"
    )

st.title("Student Information Form")
st.header("Please fill out the form below")

with st.form("student_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    grade = st.selectbox("Grade", ["Freshman", "Sophomore", "Junior", "Senior"])

    submit_button = st.form_submit_button("Submit")

if submit_button:
    db = connect_to_db()
    cursor = db.cursor()
    insert_query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, age, grade))
    db.commit()
    cursor.close()
    db.close()
    st.snow()
    
    st.success("Form Submitted Successfully!")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Grade:", grade)
