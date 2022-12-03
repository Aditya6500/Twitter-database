import pyodbc 
import streamlit as st

from register import register
from login import login 
from database import read_all
from posts import posts
from follows import follows
from friends import friends
from showtweets import showtweets
from delete_tweet import delete_tweet
from update_tweet import update_tweet
from remove_friend import remove_friend
from friends_tweet import friends_tweet
from recommend_friends import recommend_friends
from replytweet import replytweet
from showreply import showreply
from procedure import procedure

conn =pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-IBC2UKAP;"
    "Database=Twitter;"
    "Trusted_Connection=yes;"
)


def main():
    st.title(" Twitter")
    menu = ["Sign In","Sign Up", "list user","posts tweet", "update tweet", "Show Friends","follow","Show Tweets","Delete Tweet","remove friend","friends tweet","recommend friends","Reply to tweet","Show reply","procedure"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Sign Up":
        register()  
    elif choice=="list user":
        read_all()
    elif choice=="posts tweet":
        posts()
    elif choice=="follow":
        follows()
    elif choice=="Show Friends":
        friends()
    elif choice=="Show Tweets":
        showtweets()
    elif choice=="Delete Tweet":
        delete_tweet()
    elif choice=="update tweet":
        update_tweet()
    elif choice=="remove friend":
        remove_friend()
    elif choice=="friends tweet":
        friends_tweet()
    elif choice=="recommend friends":
        recommend_friends()
    elif choice=="Reply to tweet":
        replytweet()
    elif choice=="Show reply":
        showreply()
    elif choice=="procedure":
        procedure()
    else:
        username=login()
        if 'username' not in st.session_state:
            print(username)
            st.session_state['username']=username
        
if __name__ == '__main__':
    main()

conn.close()

# def read(conn):
#     print("read")
#     cursor=conn.cursor()
#     cursor.execute("select * from USER_INFO")
#     for row in cursor:
#         print(f'roe={row}')
#     print()

# def create(conn):
#     print("Create")
#     cursor=conn.cursor()
#     cursor.execute(
#         'insert into USER_INFO (id,f_name,l_name,age) values(?,?,?,?);',
#         (8,'Pavan','N',20)
#     )
#     conn.commit()
#     read(conn)