import streamlit as st
import streamlit_book as stb
from streamlit_option_menu import option_menu
from using_secret import get_googleSheet


df_name_list, df_list = get_googleSheet()


#------------------------------------- Single Choice Question -------------------------------------#
selected = option_menu(None, df_name_list,
                        icons=['lightbulb'] * len(df_name_list),
                        key='menu', orientation="horizontal")

for index, name in enumerate(df_name_list):
    if selected==name:
        st.title("Single Choice Question")
        st.header("Question with minimal arguments")

        stb.single_choice("What does pandas (the library) stands for?",
                            ["The cutest bear", "Panel Data", 
                            "Pure Adamantium Numeric Datasets And Stuff", "PArties & DAtaSets"],
                            1)