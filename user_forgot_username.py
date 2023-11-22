import streamlit as st
import mysql.connector
import hashlib
import re

# Assuming you have established a database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="lib_login"
)
cursor = db_connection.cursor()

def is_valid_email(email):
    # Regular expression for basic email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Function to check if provided information matches the database for a patient
def check_user_info(email, secret_question, secret_answer):
    query = "SELECT Name FROM User WHERE Email = %s AND SecretQuestion = %s AND LOWER(SecretAnswer) = LOWER(%s)"
    cursor.execute(query, (email, secret_question, secret_answer))
    # Fetch the result
    result = cursor.fetchall()

    # Check if the result is not None (i.e., a user with matching info is found)
    if result:
        return result[0][0]  # Return the username
    else:
        return None  # No matching user found

# Streamlit app for patient forgot password
def forgot_username():
    st.title("Forgot Username")

    email = st.text_input("Email: ")
    valid_email=is_valid_email(email)
    if valid_email:
        st.success("valid email address.")
    else:
        st.error("not a valid email address.")
    secret_question = st.selectbox("Select Secret Question: ", ["What is the name of your first pet?", "In what city were you born?", "What is your favorite movie?", "Who is your childhood best friend?", "What is the name of your favorite teacher?"])
    secret_answer = st.text_input("Secret Answer: ")

    if st.button("Submit"):
        user_name = check_user_info(email, secret_question, secret_answer)

        if user_name is None:
            st.error("Invalid user information. Please check your details and try again.")
        else:
            st.success(f"User information verified! Your username is {user_name}")


# Main Streamlit app
def main():
    forgot_username()

if __name__ == "__main__":
    main()
