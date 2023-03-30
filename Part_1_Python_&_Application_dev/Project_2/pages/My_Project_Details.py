import streamlit as st
import os
from matplotlib import image
import pandas as pd
import plotly.express as px

st.header("Crop Prediction Using :blue[Machine Learning]")

FILE_DIR= os.path.dirname(os.path.abspath(__file__))
PARENT_DIR =os.path.join(FILE_DIR, os.pardir)
dir_of_interest=os.path.join(PARENT_DIR,"resources")

IMAGE_PATH=os.path.join(dir_of_interest,"images","crop.jpg")
IMAGE_PATH_1=os.path.join(dir_of_interest,"images","required_values.jpg")
IMAGE_PATH_2=os.path.join(dir_of_interest,"images","result.jpg")

DATA_PATH=os.path.join(dir_of_interest,"data","Crop_recommendation.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

st.header("DataSet")
st.caption("We requrie different Parameters like Nitrogen, Phosphors, Potassium, temperature, Humidity, PH-value, Rainfall to predict the best Crop for the Season.")

df = pd.read_csv(DATA_PATH)
st.dataframe(df)


#chart_data = px.bar(df, x="label", y="temperature")
#st.bar_chart(chart_data,use_container_width=True)


st.header("Exploratory Data Analysis -")
st.subheader("HISTOGRAM")
st.caption("Comparision Between the label data and different Variables")

label = st.selectbox("Select the Crop:", df['label'].unique())

col1,col2,col3,col4= st.columns(4)

fig = px.histogram(df[df['label'] == label], x="temperature")
col1.plotly_chart(fig, use_container_width=True)


fig_1 = px.histogram(df[df['label'] == label], x="ph")
col2.plotly_chart(fig_1, use_container_width=True)


fig_3 = px.histogram(df[df['label'] == label], x="humidity")
col3.plotly_chart(fig_3, use_container_width=True)


fig_4 = px.histogram(df[df['label'] == label], x="rainfall")
col4.plotly_chart(fig_4, use_container_width=True)

#st.subheader("Scatter_Matrix")
#col1,col5=st.columns(2)
#fig_5 = px.scatter_matrix(df, dimensions=["temperature","ph","humidity","rainfall"])
#col5.plotly_chart(fig_5,use_container_width=True)


st.header("Front End -")
st.subheader("Farmers have to provide the Required Values")
st.caption("I have used Django to develop the Web application to Predict the best Crop for the Season.")

img_1 = image.imread(IMAGE_PATH_1)
st.image(img_1)

st.header("Results -")
st.subheader("Based on the Parameters given by the farmer the best suitable Crop is Predicted by Machine Learning Algorithm")

img_2 = image.imread(IMAGE_PATH_2)
st.image(img_2)