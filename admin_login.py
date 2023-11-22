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

# Function to verify the entered password against the stored hashed password
def verify_password(entered_password, hashed_password):
    return entered_password == hashed_password

def validate_login(username, password):
    query_librarian = "SELECT Admin_ID, Password FROM Admin WHERE Name = %s"

    cursor.execute(query_librarian, (username,))
    result_user = cursor.fetchone()
    if result_user and verify_password(password, result_user[1]):
        return result_user[0]
    return None

def loggin():
    query="""
        SELECT
            User_ID,
            Name,
            Email,
            Contact_number
        FROM
            User
    """

    cursor.execute(query,)
    user_info = cursor.fetchall()
    if user_info:
        headers = ["User ID", "User name", "Email ID", "Contact Number"]
        df = pd.DataFrame(user_info, columns=headers)

        # Display the clinical trial information in a table
        st.table(df.set_index(pd.Index(range(1, len(df) + 1))))
    else:
        st.warning("No users found")
            # Add patient-specific content for Home Page here
    if st.button("Logout"):
        st.experimental_rerun()

def login1():
    global is_logged_in

    st.title("Login Page")

    username = st.text_input("username:")
    password = st.text_input("password:", type="password")

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