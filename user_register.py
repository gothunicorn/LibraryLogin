import streamlit as st
import mysql.connector
import hashlib
from streamlit import session_state as state
import re

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="lib_login"
)
cursor = db_connection.cursor()

# Function to hash the password
def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def is_valid_phone_number(phone_number):
    return phone_number.isdigit() and len(phone_number) == 10

def is_valid_email(email):
    # Regular expression for basic email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Predefined list of secret questions
secret_questions = [
    "What is the name of your first pet?",
    "In what city were you born?",
    "What is your favorite movie?",
    "Who is your childhood best friend?",
    "What is the name of your favorite teacher?"
]

def is_valid_username(username):
    # Check if the username comprises only letters and is at least 5 characters long
    if (username.isalpha() and len(username) >= 5):
        # Check if the username is already taken in the database
        query_check_username = "SELECT COUNT(*) FROM User WHERE Name = %s"
        cursor.execute(query_check_username, (username,))
        result = cursor.fetchone()
        if result[0] != 0:
            return False  # Valid and available username
        else:
            return True
    return None


# Streamlit app for patient data entry
def register_page():
    st.title("Register")

    name = st.text_input("User Name", max_chars=20)
    valid_username = is_valid_username(name)
    if valid_username is True:
        st.success("Valid and available username.")
    elif valid_username is False:
        st.error("Username taken. Please choose another one")
    elif valid_username is None:
        st.error("Invalid Username. The UserName should have only letters and be atleast 5 charachters long")
    

    password = st.text_input("Password", type="password")

    email = st.text_input("Email")
    valid_email=is_valid_email(email)
    if valid_email:
        st.success("Valid email address.")
    else:
        st.error("Not a valid email address.")

    contact_number = st.text_input("Enter Contact Number (10 digits):", max_chars=10)
    valid_contact_number = is_valid_phone_number(contact_number)
    # Validate the input
    if valid_contact_number:
        st.success("Valid phone number!")
        # Use the phone_number variable in your application logic
    else:
        st.error("Not a valid phone number.")
        
    secretquestion = st.selectbox("Select Secret Question", secret_questions)
    secretanswer = st.text_input("Secret Answer", type="password")

    # Validate that all required fields are filled
    all_fields_filled = all([name, password, email, secretquestion, secretanswer,contact_number])
    

    # Enable or disable the submission button based on validation
    submit_button = st.button("Submit", disabled=not (all_fields_filled and valid_contact_number and valid_email and valid_username))

    # Show a message if any required field is not filled
    if not all_fields_filled:
        st.warning("Please fill in all the required fields.")

    if submit_button:
        hashed_password = hash_password(password)
        insert_user = "INSERT INTO User (Name, password, Email, Contact_number, SecretQuestion, SecretAnswer) VALUES ( %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_user, (name, hashed_password, email, contact_number, secretquestion, secretanswer))
        db_connection.commit()
        st.success("User data successfully submitted!")
        
if __name__ == "__main__":
    register_page()