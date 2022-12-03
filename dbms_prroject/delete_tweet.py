import streamlit as st
from database import get_usernames
from database import get_tweets
from database import remove_tweet_edge
from database import remove_tweet
def delete_tweet():
    user_name='Aditya6500'
    user_names=get_usernames()
    username=st.selectbox("Select the user",user_names)
    all_tweets=get_tweets(username)
    tweet=st.selectbox("Select tweet",all_tweets)
    if(st.button("delete")):
        remove_tweet_edge(username,tweet)
        remove_tweet(tweet)

