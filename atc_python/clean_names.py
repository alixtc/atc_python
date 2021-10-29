import unicodedata
import pandas as pd

def strip_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text)
                   if unicodedata.category(c) != 'Mn')

def clean_one_name(name: str) -> str:
    new_name = ""
    for s in name:
        if (s.isalpha() or s.isdigit() or s.isspace()):
            new_name += s
        else:
            new_name += " "

    new_name = strip_accents(new_name).lower()
    new_name = new_name.replace("  ", " ").strip()
    new_name = new_name.replace(" ", "_")
    return new_name

def clean_names(dataframe: pd.DataFrame) -> list:
    """
    Returns the columns names of a dataframe with only latin letters
    written in snake_case
    """
    column_names = dataframe.columns
    new_names = [clean_one_name(name) for name in column_names]
    return new_names
