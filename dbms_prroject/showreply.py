import streamlit as st
from database import get_tweets_of
from database import show_reply
def showreply():
    all_tweets=get_tweets_of()
    tweet=st.selectbox("Select tweet",all_tweets)
    if st.button("Show"):
        show_reply(tweet)