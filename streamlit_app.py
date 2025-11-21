import streamlit as st
import pandas as pd
st.title('DS_2025 First Project')

st.write('Good job!')

with st.expander("**Data**"):
  st.write("data ai")
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
with st.expander("Plot"):
  st.scatter_chart(data = df,x = 'bill_length_mm', y = 'bill_depth_mm', color = 'species')
with st.sidebar:
  st.header('Input features')
  island = st.selectbox(df['island'].unique())
