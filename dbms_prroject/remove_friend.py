import streamlit as st
from database import get_usernames
from database import delete_edge
def remove_friend():
    st.subheader("Unfollow friend")
    user_names=get_usernames()
    st.dataframe(user_names)
    username1=st.text_input("Select user")
    username2=st.text_input("Unfollow Friend")
    if st.button("Unfollow"):
        if delete_edge(username1,username2)==True:
            st.success("Unfollowed Successfully")