import streamlit as st
import requests as rq
import numpy as np

st.set_page_config(
    page_title = "HCI - Project 2",
    layout = "wide",
    menu_items={
        "Get Help" : "https://docs.streamlit.io/",
        "About" : "Welcome to Project Bulldozer's Weather App"
    }
)

st.title("Weather App")
st.header("HCI - Project Bulldozer")

add_selectbox = st.sidebar.selectbox(
    "Select a Feature",
    ["Homepage", "Weather Report", "Global Warming", "Natural Disasters"]
)

if add_selectbox == "Weather Report":
    st.subheader("Weather Report")


elif add_selectbox == "Global Warming":
    st.subheader("Global Warming")


elif add_selectbox == "Natural Disasters":
    st.subheader("Natural Disasters")


else:
    st.subheader("Who We Are")

