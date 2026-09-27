import streamlit as st
import pandas as pd

input_csv = st.file_uploader("Upload", type="csv")

st.write(pd.read_csv(input_csv.name))