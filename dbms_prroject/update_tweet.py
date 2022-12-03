import streamlit as st
from database import get_usernames
from database import get_tweets
from database import change_tweet
def update_tweet():
    user_name='Aditya6500'
    user_names=get_usernames()
    username=st.selectbox("Select the user",user_names)
    all_tweets=get_tweets(username)
    tweet=st.selectbox("Select tweet",all_tweets)
    tweet_update=st.text_input("Enter the updated tweet")
    if st.button("Update"):
        if change_tweet(tweet,tweet_update)==True:
            st.success("Tweet updated Successfully")