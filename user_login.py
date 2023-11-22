import streamlit as st
import mysql.connector
import pandas as pd
import hashlib

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="lib_login"
)

cursor = db_connection.cursor()
is_logged_in = False

def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

# Function to verify the entered password against the stored hashed password
def verify_password(entered_password, hashed_password):
    res = hashlib.sha256(entered_password.encode()).hexdigest() == hashed_password
    return res

def validate_login(username, password):
    query_user = "SELECT User_ID, Password FROM User WHERE Name = %s"
    cursor.execute(query_user, (username,))
    result_user = cursor.fetchone()
    if result_user and verify_password(password, result_user[1]):
        return result_user[0]
    return None

def loggin():
    if st.button("Logout"):
        st.experimental_rerun()

def login1():
    global is_logged_in

    st.title("Login Page")

    username = st.text_input("Username:", max_chars=20, value="")
    password = st.text_input("Password:", type="password", value="")

    if st.button("Login"):
        login_result = validate_login(username, password)

        if login_result:
            id = login_result
            st.success(f"Login successful! ID: {id}")
            is_logged_in = True  # Update login status
            loggin()
        else:
            st.error("Invalid login credentials")

def login():
    login1()


if __name__ == "__main__":
    login()