import streamlit as st
from database import get_usernames
from database import add_friend
from database import friends_u2
from database import tweets_u2
def follows():
    st.subheader("Add friend")
    user_names=get_usernames()
    st.dataframe(user_names)
    username1=st.text_input("Select user")
    username2=st.text_input("Add Friend")
    if st.button("Add friend"):
        if add_friend(username1,username2)==True:
            st.success("Added friend Successfully ")
            st.header("friends")
            friends_u2(username2)
            st.header("tweets")
            tweets_u2(username2)
        else:
            st.error("Already a friend")