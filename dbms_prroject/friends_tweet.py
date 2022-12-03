import streamlit as st
from database import get_usernames
from database import show_friends_tweet

def friends_tweet():
    user_name='Aditya6500'
    user_names=get_usernames()
    username=st.selectbox("Select the user",user_names)
    if st.button("Show friends tweet"):
        show_friends_tweet(username)