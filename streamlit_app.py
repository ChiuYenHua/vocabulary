import streamlit as st
import streamlit_book as stb
from pathlib import Path
from google.oauth2 import service_account
import gspread
import pandas as pd
    
#------------------------------------- Get Data -------------------------------------#
# Uses st.cache_data to only return when the query changes or after 10 min.
@st.cache_resource(ttl=600)
def get_googleSheet():
    # Make list to store all google worksheets into DataFrame and name, too
    df_list = []
    df_name_list = []

    # Url of private google sheet
    sheet_url = st.secrets["private_gsheets_url"]

    #Create credential from GCP service account
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
        ],
    )

    # Using credentials to access google sheet spread
    gs = gspread.authorize(credentials)

    # Get sheet object
    sheet = gs.open_by_url(sheet_url)
    
    # Loop through 'all worksheets' in google sheet
    for i in range(len(sheet.worksheets())):
        every_worksheet = sheet.get_worksheet(i)

        df_list.append(pd.DataFrame(every_worksheet.get_all_records()))
        df_name_list.append(every_worksheet.title)
    
    return df_name_list, df_list

df_name_list, df_list = get_googleSheet()
    



#------------------------------------- MAIN -------------------------------------#
def main():
    save_answers = False
    current_path = Path(__file__).parent.absolute()

    stb.set_book_config(menu_title="Cool Stuff",
                    menu_icon="yin-yang",
                    options=[
                            "Single Choice Question",
                            ], 
                    paths=[
                            current_path / "pages/choice_exam/single_choice.py",
                            ],
                    save_answers=save_answers,
                    display_page_info=False,
                    )



if __name__ == "__main__":
    main()