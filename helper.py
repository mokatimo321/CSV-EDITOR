import streamlit as st
import pandas as pd

st.write(""" # CSV FILES EDITOR - by TimoKama """)


@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')

# Collects user input features into dataframe
uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) 
    columns_list = list(df)
    st.subheader("Select the Columns to be Kept!!")
    options = st.multiselect('Choose the Columns to be kept!!',columns_list,columns_list[0])
    df_mod = df.filter(options, axis=1)
    csv1 = convert_df(df_mod)
    st.download_button("DOWNLOAD!!",csv1,"updated.csv","text/csv")
