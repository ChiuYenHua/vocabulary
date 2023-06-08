import streamlit as st
import streamlit_book as stb
from pathlib import Path


#------------------------------------- MAIN -------------------------------------#
def main():
    save_answers = False
    current_path = Path(__file__).parent.absolute()

    stb.set_book_config(menu_title="Cool Stuff",
                    menu_icon="alipay",
                    options=[
                            "Single Choice Question",
                            "Whiteboard",
                            ], 
                    paths=[
                            current_path / "pages/choice_exam/single_choice.py",
                            current_path / "pages/whiteboard/whiteboard.py",
                            ],
                    save_answers=save_answers,
                    display_page_info=False,
                    )



if __name__ == "__main__":
    main()