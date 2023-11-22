#USER DASHBOARD
import streamlit as st
import mysql.connector
import pandas as pd
import hashlib
from admin_login import login
from admin_forgot import forgot

def admin_page():
    st.title("Librarian Dashboard")

    # Sidebar navigation
    selected_page = st.sidebar.radio("Navigation", ["Login", "Forgot Password"])
    if selected_page == "Login":
        login()
    elif selected_page == "Forgot Password":
        forgot()

if __name__ == "__main__":
    admin_page()
