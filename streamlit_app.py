# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect
import gspread
import pandas as pd

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)

gs = gspread.authorize(credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_resource(ttl=600)
def get_googleSheet(sheet_url):
    sheet = gs.open_by_url(sheet_url)
    worksheet = sheet.get_worksheet(0)
    return worksheet.get_all_records()

sheet_url = st.secrets["private_gsheets_url"]

df = pd.DataFrame(get_googleSheet(sheet_url))
st.write(df)