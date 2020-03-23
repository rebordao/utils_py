from typing import List

class NLP:
    """
    A set of utilities to manipulate text and strings.
    """

    def __init__(self) -> None:
        pass

    def get_standardised_var_names(self, cols) -> List:
        """
        Returns a list of column names in standard format.

        - Transforms upper cases (AClass) in lower cases (aclass).
        - Transforms dashes (-) in underscores (_).
        - Transforms period (.) in empty strings ('').
        """
        return [re.sub('[- ]', '_', n).replace('.', '').lower() for n in cols]