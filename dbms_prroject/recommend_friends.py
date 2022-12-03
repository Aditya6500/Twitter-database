import streamlit as st
from database import get_usernames
from database import recommend
def recommend_friends():
    user_name='Aditya6500'
    user_names=get_usernames()
    username=st.selectbox("Select the user",user_names)
    if st.button("Recommend Friends"):
        recommend(username)