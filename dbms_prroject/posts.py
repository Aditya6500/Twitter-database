import streamlit as st
from database import add_tweet
from database import add_edge
from database import get_usernames
from database import create_link
from database import add_link
from database import add_mention
# from database import add_link
def posts():
    st.subheader("Posts Tweet")
    username='Aditya6500'
    user_names=get_usernames()
    username=st.selectbox("Select the user",user_names)
    tweet=st.text_input("Enter the Tweet")
    mention=st.text_input("Mention a User")
    link=st.text_input("Add link")
    if username=='null':
        st.write("Log in")
        return 
    if st.button("Post"):
        if add_tweet(tweet)==True:
            st.success("Tweet posted succesfully")
            add_edge(username,tweet)
            if link!='':
                create_link(link)
                add_link(tweet,link)
            if mention!='':
                add_mention(tweet,mention)
    