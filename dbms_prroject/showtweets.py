import streamlit as st
from database import get_usernames
from database import all_tweets
def showtweets():
    user_names=get_usernames()
    username=st.selectbox("Select the user",user_names)
    if st.button("Show Tweets"):
        all_tweets(username)