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
  island = st.selectbox('Island', df['island'].unique())
  bill_length_mm = st.slider("**bill_length_mm**", 32.1, 59.6, 34.1)
  bill_depth_mm = st.slider("**bill_depth_mm**", 32.1, 59.6, 45.1)
  flipper_length_mm = st.slider("**flipper_length_mm**", 32.1, 59.6, 55.1)
  body_mass_g = st.slider("**body_mass_g**", 2700, 6300, 4207)
  sex = st. selectbox("**Gender**", ('male', 'female'))
data = {'island':island,
        'bill_length_mm':bill_length_mm,
        'bill_depth_mm':bill_depth_mm,
        'flipper_length_mm':flipper_length_mm,
        'body_mass_g':body_mass_g,
        'sex':sex}
input_df = pd.DataFrame(data, index=[0])
input_penguins = pd.concat([input_df, X_raw], axis=0)
