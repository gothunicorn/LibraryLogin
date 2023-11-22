#USER DASHBOARD
import streamlit as st
import mysql.connector
import pandas as pd
import hashlib
from user_login import login
from user_register import register_page
from user_forgot import forgot_password
from user_forgot_username import forgot_username

def user_page():
    st.title("User Dashboard")

    # Sidebar navigation
    selected_page = st.sidebar.radio("Navigation", ["Login", "Register", "Forgot Password", "Forgot Username"])

    if selected_page == "Login":
        login()
    elif selected_page == "Register":
        register_page()
    elif selected_page == "Forgot Password":
        forgot_password()
    elif selected_page == "Forgot Username":
        forgot_username()

if __name__ == "__main__":
    user_page()
