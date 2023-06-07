import streamlit as st
import streamlit_book as stb
from streamlit_option_menu import option_menu


#------------------------------------- Single Choice Question -------------------------------------#
selected = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
                        icons=['house', 'cloud-upload', "list-task", 'gear'],
                        key='menu_5', orientation="horizontal")

if selected=='Home':
    st.title("Single Choice Question")
    st.header("Question with minimal arguments")

    stb.single_choice("What does pandas (the library) stands for?",
                        ["The cutest bear", "Panel Data", 
                        "Pure Adamantium Numeric Datasets And Stuff", "PArties & DAtaSets"],
                        1)