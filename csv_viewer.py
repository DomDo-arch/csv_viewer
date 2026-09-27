import streamlit as st
import pandas as pd

input_csv = st.file_uploader("Upload", type="csv")

if input_csv is not None:
  st.write(pd.read_csv(input_csv))
