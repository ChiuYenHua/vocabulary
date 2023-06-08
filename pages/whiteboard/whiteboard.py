import streamlit as st
import streamlit_book as stb
from pages.whiteboard.whiteboard_function import run_scheduler
from threading import Thread

st.title('Whiteboard')

show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):

    thread = Thread(target=run_scheduler)
    thread.start()

    # def read_file():
    #     previous_txt = ''
    #     with open('./pages/whiteboard/whiteboard_text.txt', 'r+') as f:
    #         for i in f.readlines():
    #             previous_txt += i

    #     st.session_state["default"] = previous_txt

    # if st.button('Refresh'):
    #     read_file()

    # if "default" not in st.session_state:
    #     read_file()

    response = st.text_area("", value=st.session_state["default"], height=600)

    if st.button("Update whiteboard"):
        st.balloons()

        with open('./pages/whiteboard/whiteboard_text.txt', 'w+') as f:
            f.writelines(response)



