import streamlit as st
email = st.text_input('Enter email')
password = st.text_input('Enter password')
#number = st.number_input('Enter age')

btn = st.button('Login Karo')

# if the button is clicked
if btn:
    if email == 'amangupta@.com' and password == '1234':
        st.balloons()

    else:
        st.error('Login Failed')