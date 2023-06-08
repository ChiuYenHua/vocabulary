import schedule
import time
import streamlit as st

def job():
    previous_txt = ''
    with open('./pages/whiteboard/whiteboard_text.txt', 'r+') as f:
        for i in f.readlines():
            previous_txt += i

    st.session_state["default"] = previous_txt

def run_scheduler():
    schedule.every(1).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)