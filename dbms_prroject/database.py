import pyodbc 
import streamlit as st
import pandas as pd
conn =pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-IBC2UKAP;"
    "Database=Twitter;"
    "Trusted_Connection=yes;"
)


def friends_u2(u3):
    cursor=conn.cursor()
    cursor.execute("SELECT u2.username FROM  USER_INFO as u1, USER_INFO as u2, FOLLOWS WHERE MATCH (u1-(FOLLOWS)->u2) AND u1.username='{}';".format(u3))
    st.dataframe(cursor)

def tweets_u2(u3):
    cursor=conn.cursor()
    cursor.execute("SELECT tweet FROM TWEET, POSTS, USER_INFO WHERE MATCH (USER_INFO-(POSTS)->TWEET) AND USER_INFO.username='{}';".format(u3))
    st.dataframe(cursor)
    
def procedure_call(username):
    cursor=conn.cursor()
    cursor.execute("EXECUTE get_tweets '{}';".format(username))
    st.dataframe(cursor)

def show_reply(tweet):
    cursor=conn.cursor()
    cursor.execute("SELECT reply FROM TWEET, REPLY ,REPLY_TO WHERE MATCH (TWEET-(REPLY_TO)->REPLY) AND TWEET.tweet='{}';".format(tweet))
    st.dataframe(cursor)

def create_reply(reply,username,):
    cursor=conn.cursor()
    cursor.execute( "INSERT INTO REPLY (reply,username) VALUES (?,?);",(reply,username))
    cursor.commit()
    return True

def get_tweets_of():
    cursor=conn.cursor()
    cursor.execute("SELECT tweet FROM TWEET")
    l=[]
    for row in cursor:
        for i in row:
            l.append(i)
    return l

def reply_link(tweet, reply):
    cursor=conn.cursor()
    cursor.execute("INSERT INTO REPLY_TO VALUES((SELECT $node_id FROM TWEET WHERE tweet='{}'),(SELECT $node_id FROM REPLY WHERE reply='{}'));".format(tweet,reply))
    cursor.commit()
    

def add_mention(tweet,u2):
    cursor=conn.cursor()
    cursor.execute("INSERT INTO MENTIONS VALUES((SELECT $node_id FROM TWEET WHERE tweet='{}'),(SELECT $node_id FROM USER_INFO WHERE username='{}'));".format(tweet,u2))
    cursor.commit()

def add_link(tweet,link):
    cursor=conn.cursor()
    cursor.execute("INSERT INTO CONTAINS_LINK VALUES((SELECT $node_id FROM TWEET WHERE tweet='{}'),(SELECT $node_id FROM LINK WHERE link='{}'));".format(tweet,link))
    cursor.commit()

def recommend(name):
    cursor=conn.cursor()
    cursor.execute("SELECT u3.username FROM USER_INFO as u1,FOLLOWS,FOLLOWS as f1,USER_INFO as u2,USER_INFO as u3 WHERE MATCH (u1-(f1)->u2-(FOLLOWS)->u3) AND u1.username='{}' AND u3.username!='{}';".format(name,name))
    st.dataframe(cursor)


def show_friends_tweet(name):
    cursor=conn.cursor()
    cursor.execute("SELECT CONCAT(USER_INFO.username,'->' ,u1.username,'->',TWEET.tweet) FROM USER_INFO ,FOLLOWS,POSTS,USER_INFO as u1 , TWEET WHERE MATCH (USER_INFO-(FOLLOWS)->u1-(POSTS)->TWEET) AND USER_INFO.username='{}';".format(name))
    st.dataframe(cursor)

def delete_edge(u1,u2):
    cursor=conn.cursor()
    cursor.execute(
        "DELETE FROM FOLLOWS WHERE $From_id=(SELECT $node_id from USER_INFO WHERE username='{}') AND $To_id=(SELECT $node_id from USER_INFO WHERE username='{}');".format(u1,u2)
    )
    cursor.commit()
    return True

def change_tweet(a,b):
    cursor=conn.cursor()
    cursor.execute("UPDATE TWEET SET tweet='{}' WHERE tweet='{}';".format(b,a))  
    cursor.commit()
    return True

def remove_tweet_edge(name,tweet):
    cursor=conn.cursor()
    cursor.execute("DELETE from POSTS WHERE $From_id=(SELECT $node_id from USER_INFO WHERE username='{}') AND $To_id=(SELECT $node_id from TWEET WHERE tweet='{}');".format(name,tweet))
    cursor.commit()

def remove_tweet(tweet):
    cursor=conn.cursor()
    cursor.execute("DELETE from TWEET WHERE tweet='{}';".format(tweet))
    cursor.commit()

def get_tweets(name):
    cursor=conn.cursor()
    cursor.execute("SELECT TWEET.tweet FROM TWEET , POSTS, USER_INFO WHERE MATCH (USER_INFO-(POSTS)->TWEET) AND USER_INFO.username='{}';".format(name))
    l=[]
    for row in cursor:
        for i in row:
            l.append(i)
    return l

def all_tweets(name):
    cursor=conn.cursor()
    cursor.execute("SELECT dbo.no_of_tweets1('{}')".format(name))
    st.dataframe(cursor)
    cursor.execute("SELECT TWEET.tweet FROM TWEET , POSTS, USER_INFO WHERE MATCH (USER_INFO-(POSTS)->TWEET) AND USER_INFO.username='{}';".format(name))
    st.dataframe(cursor)

def show_friends(name):
    cursor=conn.cursor()
    cursor.execute("SELECT CONCAT(USER_INFO.username,'->' ,U2.username) FROM USER_INFO ,FOLLOWS, USER_INFO AS U2 WHERE MATCH (USER_INFO-(FOLLOWS)->U2) AND USER_INFO.username='{}';".format(name))
    st.dataframe(cursor)

def add_friend(u1,u2):
    cursor=conn.cursor()
    cursor.execute("SELECT $TO_id FROM FOLLOWS WHERE $FROM_id=(SELECT $node_id FROM USER_INFO WHERE username='{}');".format(u1))
    l=[]
    for row in cursor:
        for col in row:
            l.append(col)
    cursor.execute("SELECT $node_id FROM USER_INFO WHERE username='{}';".format(u2))
    l1=[]
    for row in cursor:
        for col in row:
            l1.append(col)
    for i in l:
        if i==l1[0]:
            return False
    # cursor.execute("SELECT $node_id FROM USER_INFO WHERE username='{}'".format(u2))
    cursor.execute(
        "INSERT INTO FOLLOWS VALUES((SELECT $node_id FROM USER_INFO WHERE username='{}'),(SELECT $node_id FROM USER_INFO WHERE username='{}'));".format(u1,u2)
    )
    conn.commit()
    return True
    
def create_link(link):
    cursor=conn.cursor()
    cursor.execute("INSERT INTO LINK (link) VALUES(?);",(link))
    cursor.commit()

def get_usernames():
    cursor=conn.cursor()
    cursor.execute("SELECT username from USER_INFO ")
    l=[]
    for row in cursor:
        for i in row:
            l.append(i)
    return l


def read_all():
    cursor=conn.cursor()
    cursor.execute("select username,f_name,l_name,age,pasword from USER_INFO")
    st.dataframe(cursor)
    for row in cursor:
        st.write(row)

def add_tweet(tweet):
    if tweet=='':
        st.write("Please enter the tweet")
        return False
    cursor=conn.cursor()
    cursor.execute(
        "insert into TWEET (tweet) VALUES(?);",(tweet)
    )
    conn.commit()
    return True

def add_edge(user_name,tweet):
    cursor=conn.cursor()
    cursor.execute(
        "INSERT INTO POSTS VALUES((SELECT $node_id FROM USER_INFO WHERE username='{}'),(SELECT $node_id FROM TWEET WHERE tweet='{}'));".format(user_name,tweet)
    )
    conn.commit()

def read(user_name):
    cursor=conn.cursor()
    cursor.execute("SELECT username ,f_name,l_name ,age,pasword FROM USER_INFO WHERE username='{}';".format(user_name))

    
def check_password(user_name,password):
    cursor=conn.cursor()
    cursor.execute("SELECT pasword FROM USER_INFO WHERE username='{}';".format(user_name))
    data=1

    for i in cursor:
        data=i
    if(type(data)==int):
        st.error("USER NOT AVAILABLE")
        return False
    else:
        for i in data:
            p=i
        if(p==password):
            return True
        else:
            st.error("Wrong Password")
            return False

        
def add_data(user_name,f_name,l_name,age,password):
    cursor=conn.cursor()
    data=1
    cursor.execute("SELECT username FROM USER_INFO WHERE username='{}';".format(user_name))
    for i in cursor:
        data=i
        st.write(type(data))
    if(type(data)==int):
        cursor.execute('INSERT INTO USER_INFO (username,f_name,l_name,age,pasword) VALUES (?,?,?,?,?);',(user_name,f_name,l_name,age,password))
        conn.commit()
        return True
    else:
        st.write('User Name is already present')
        return False

