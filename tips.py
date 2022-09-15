import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

tips_df = pd.read_csv('./datasets/tips.csv', index_col=0)

st.header('You can vizualize and analize amount of tips depending on week day, time, if client is smoker, men or women')

chart = st.selectbox('Select of chart you want to see', ['Line chart', 'Histogramm', 'Scatter', 'Box'])

x = st.selectbox('What features will be displayed on x axis', tips_df.columns, index=0)

y = st.selectbox('Features on y axis', tips_df.columns, index=0)

if_size = st.checkbox('Size is usefull for scatterplot to display third parameter for displaying dependencies')

size = False
if if_size:
  size = st.selectbox('Size', tips_df.columns)



if st.button('Compare'):
    if chart == 'Line chart':
        st.line_chart(x=x, y=y, data=tips_df)
    if chart == 'Histogramm':
        fig, ax = plt.subplots()
        ax.hist(tips_df[x], bins=20)
        st.pyplot(fig)
    if (chart == 'Scatter') and not size:
        fig, ax = plt.subplots()
        ax.scatter(x, y, data=tips_df)
        st.pyplot(fig)
    if (chart == 'Scatter') and size:
        fig, ax = plt.subplots()
        ax.scatter(x, y, s=size, data=tips_df)
        st.pyplot(fig)
