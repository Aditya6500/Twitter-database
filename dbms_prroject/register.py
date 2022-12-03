import streamlit as st
from database import add_data
from database import read
from login import login
def register():
    st.subheader("Sign UP")
    f_name=st.text_input("First name")
    l_name=st.text_input("Last name")
    user_name=st.text_input("Username")
    age=st.number_input("Age")
    password=st.text_input("Password")
    if st.button("Register"):
        if add_data(user_name,f_name,l_name,age,password)==False:
            st.text("Username already exists")
        else:
            st.success("Successfully added User: {}".format(user_name))
            read(user_name)


