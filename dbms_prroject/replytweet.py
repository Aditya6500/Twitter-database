import streamlit as st
from database import get_usernames
from database import get_tweets_of
from database import create_reply
from database import reply_link
def replytweet():
    user_name='Aditya6500'
    user_names=get_usernames()
    username=st.selectbox("Select the user",user_names)
    all_tweets=get_tweets_of()
    tweet=st.selectbox("Select tweet",all_tweets)
    reply_text=st.text_input("Reply")
    if st.button("Reply"):
        if create_reply(reply_text,username):
            reply_link(tweet,reply_text)
            st.success("Sucess")