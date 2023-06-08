import streamlit as st
import streamlit_book as stb

st.title('Whiteboard')

show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
    if st.button('Refresh'):
        st.experimental_rerun()

    if "default" not in st.session_state:
        previous_txt = ''
        with open('./pages/whiteboard/whiteboard_text.txt', 'r+') as f:
            for i in f.readlines():
                previous_txt += i

        st.session_state["default"] = previous_txt

    response = st.text_area("", value=st.session_state["default"], height=600)

    if st.button("Update whiteboard"):
        st.balloons()

        with open('./pages/whiteboard/whiteboard_text.txt', 'w+') as f:
            f.writelines(response)



