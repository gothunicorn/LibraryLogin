import streamlit as st
import mysql.connector
from streamlit import session_state as state
from user1 import user_page
from admin1 import admin_page

def main():
    page = st.sidebar.selectbox("Select Page", ["User", "Admin"])

    if page == "User":
        user_page()
    
    elif page == "Admin":
        admin_page()
    

if __name__ == "__main__":
    main()