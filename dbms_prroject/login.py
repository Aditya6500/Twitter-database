import streamlit as st
from posts import posts
from database import check_password
def login():
    st.subheader("Sign In")
    name=st.text_input("User_name")
    password=st.text_input("password")
    if st.button("Submit"):
        if(check_password(name,password)==True):
            st.success("Successfully logged in   : {}".format(name))
            #posts(name)
            return name

