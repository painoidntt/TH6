import streamlit as st
import pickle as pkl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import PIL as Image

st.title('Data-explpration')

st.header('Upload a dataset')
uploaded_file = st.file_uploader("Choose a .csv file", type=(['csv']), accept_multiple_files=False)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.header('Show data')
    st.dataframe(df)

    st.header('Describe attribute')
    st.table(df.describe())

    st.header('Show variables\' infomation')
    buffer = io.StringIO()
    df.info(buf=buffer)
    s= buffer.getvalue()
    st.text(s)

    st.header('Visualize each variable')
    for col in list(df.columns):
        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20)
        plt.xlabel(col)
        plt.ylabel('Quantity')
        st.pyplot(fig)

   
  
