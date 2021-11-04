import unicodedata
import pandas as pd

__all__ = ['CleanNames']

class CleanNames:
    def __init__(self, dataframe: pd.DataFrame):
        self.columns = self.clean_names(dataframe)
        self.new_old_match = self.create_matching_dict(dataframe)

    def strip_accents(self, text):
        return ''.join(c for c in unicodedata.normalize('NFKD', text)
                    if unicodedata.category(c) != 'Mn')

    def clean_one_name(self, name: str) -> str:
        """
        Remove accents, strips terminal and double white spaces,
        change spaces to underscores, and lower case everywhere
        """
        new_name = ""
        for s in name:
            if (s.isalpha() or s.isdigit() or s.isspace()):
                new_name += s
            else:
                new_name += " "
        new_name = self.strip_accents(new_name).lower()
        new_name = new_name.replace("  ", " ").strip()
        new_name = new_name.replace(" ", "_").replace('__', '_')
        return new_name

    def clean_names(self, dataframe: pd.DataFrame) -> list:
        """
        Returns the columns names of a dataframe with only latin letters
        written in snake_case
        """
        column_names = dataframe.columns
        new_names = [self.clean_one_name(name) for name in column_names]
        return new_names

    def create_matching_dict(self, dataframe: pd.DataFrame) -> dict:
        old_names = dataframe.columns
        matching_dict = {new:old for (new, old) in zip(self.columns, old_names)}
        return matching_dict

    def __call__(self):
        return self.columns
