import streamlit as st
from database import show_friends
from database import get_usernames
def friends():
    user_names=get_usernames()
    username=st.selectbox("Select the user",user_names)
    if st.button("Show Friends"):
        show_friends(username)