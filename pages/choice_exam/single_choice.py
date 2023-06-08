import streamlit as st
import streamlit_book as stb
from streamlit_option_menu import option_menu
from using_secret import get_googleSheet
from pages.choice_exam.single_choice_function import question_builder


#------------------------------------- Single Choice Question -------------------------------------#
st.title("Single Choice Question")
#st.header("Question with minimal arguments")

# Get google sheet data from another python file
df_name_list, df_list = get_googleSheet()

selected = option_menu(None, df_name_list,
                        icons=['lightbulb'] * len(df_name_list),
                        key='menu', orientation="horizontal")


question_list, options_list, answer_list = question_builder(df_list[df_name_list.index(selected)])

user_response = []

for i in range(len(answer_list)):
    user_response.append(    
        st.radio(
                question_list[i],
                options_list[i])
    )


# for i in range(len(answer_list)):
#     stb.single_choice(question_list[i],
#                         options_list[i],
#                         answer_list[i])