import streamlit as st
import io
import os
import pandas as pd
from shapely.geometry import Point

st.title(":red[Open Pub Application]")
st.subheader("Everyone can find the :blue[nearest pubs location in the United Kingdom (UK)]")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "pub_cleaned.csv")


df = pd.read_csv(DATA_PATH)
st.subheader(":green[ Basic Information and Statistics about the Dataset]")
df["geometry"] = df.apply(lambda row: Point(row["longitude"], row["latitude"]), axis=1)


data_info = st.radio('Click to view the Details of the Dataset:',
                      ('Shape', 'Info', 'Descriptive Statistics'),
                      horizontal=True)

if data_info == 'Shape':
    st.write(f"Number of Rows:  {df.shape[0]}")
    st.write(f"Number of Columns:  {df.shape[1]}")
elif data_info == 'Info':
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
else:
    st.write(df.describe())

