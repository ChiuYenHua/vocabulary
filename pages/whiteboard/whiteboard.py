import streamlit as st

if "default" not in st.session_state:
    st.session_state["default"] = "Default text" * 100

my_area = st.text_area(
    ":blue[My text here :]", value=st.session_state["default"], height=2000
)

if st.button("Update default example"):
    st.session_state["default"] = "Updated text" * 100
    st.experimental_rerun()