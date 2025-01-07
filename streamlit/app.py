import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello World from Streamlit!')


st.write('This is a simple example of a Streamlit app.')


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.success("Success")
st.info("Info")
st.warning("Warning")
st.error("Error")
st.exception("Exception")

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

else:
    st.write('Checkbox is not checked')

color = st.radio("What is your favorite color", ('Red', 'Green', 'Blue'))

if color == 'Red':
    st.error("You chose Red")

if color == 'Green':
    st.success("You chose Green")

if color == 'Blue':
    st.info("You chose Blue")

# Add a selectbox 
occupation = st.selectbox("what do you do?", ['Programmer', 'Data Scientist', 'Project Manager'])

st.write("You selected:", occupation)

# button
if st.button('Say hello'):
    st.write('Why hello there - You clicked the button')