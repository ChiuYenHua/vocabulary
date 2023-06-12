import os
import pandas as pd
import random
import streamlit as st

#------------------------------------- Build questions in shuffle weighted way -------------------------------------#
def random_weighted_select(english_list, weight, count):
    question_keys = []
    keys = english_list.copy()

    while(len(question_keys)<count):
        temp_question = random.choices(keys, weights=weight, k=1)[0]
        if temp_question not in question_keys:
            question_keys.append(temp_question)

            index = keys.index(temp_question)
            del keys[index]
            del weight[index]

    return question_keys

@st.cache_data
def question_builder(df):
    #------------------------------------ Preprocess Data ------------------------------------#
    # Read data of right_wrong 
    if os.path.isfile('quiz_statistics.csv'):
        df_weight = pd.read_csv('quiz_statistics.csv')
        # Check if vocabulary increase or decrease
        # df_weight = vocabulary_increase_decrease(df, df_weight)
    else:
        df_weight = df.copy()
        df_weight['weight'] = 1000

    # list of every column in DataFrame
    weight_list = df_weight['weight'].to_list()
    english_list = df_weight['english'].to_list()
    chinese_list = df_weight['chinese'].to_list()

    # Get shuffle vocabulary keys for 10 quesiton
    selected_english = random_weighted_select(english_list , weight_list, 10)  


    #------------------------------------ Build question ------------------------------------#
    question_list = []
    for index, key in enumerate(selected_english):
        question_list.append(f'Q{index+1}. {key}')

    #------------------------------------ Build options + answer ------------------------------------#
    options_list = []
    answer_list = []

    shuffled_chinese_list = chinese_list.copy()

    for every_selected_english in selected_english:
        # selected chinese in this question
        every_selected_chinese = chinese_list[english_list.index(every_selected_english)]

        # Make 4 options of each question (4 options can't include answer)
        while(True):
            random.shuffle(shuffled_chinese_list)
            shuffle_4_options = shuffled_chinese_list[:4]

            if every_selected_chinese not in shuffle_4_options:
                break

        # Substituted 4 options with 1 answer in it
        answer_position = random.randint(0,3)
        shuffle_4_options[answer_position] = every_selected_chinese

        # Append options and answer
        options_list.append(shuffle_4_options)
        answer_list.append(answer_position)

    return question_list, options_list, answer_list

def record_right_wrong(user_response, user_response_right_wrong):
    pass