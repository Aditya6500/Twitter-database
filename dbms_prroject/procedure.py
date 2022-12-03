import streamlit as st
from database import get_usernames
from database import procedure_call
def procedure():
    user_name='Aditya6500'
    user_names=get_usernames()
    username=st.selectbox("Select the user",user_names)
    if st.button("show"):
        procedure_call(username)
        