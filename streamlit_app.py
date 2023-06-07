import streamlit as st
import streamlit_book as stb
from pathlib import Path
    

    
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