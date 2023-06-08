import streamlit as st


if "default" not in st.session_state:
    previous_txt = ''
    with open('./pages/whiteboard/whiteboard_text.txt', 'r+') as f:
        for i in f.readlines():
            previous_txt += i

    st.session_state["default"] = previous_txt


response = st.text_area("WHITEBOARD", value=st.session_state["default"], height=800)

if st.button("Update whiteboard"):
    with open('./pages/whiteboard/whiteboard_text.txt', 'w+') as f:
        f.writelines(response)
        
    st.session_state["default"] = 'Text is upadated!!!!!!!!!'
    st.experimental_rerun()


