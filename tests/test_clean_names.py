from atc_python.clean_names import CleanNames
import pandas as pd
import numpy as np
import re

COLUMN_NAMES = [
    'Carton Rouge_op1260',
    'température four cuissonop1260',
    'T° tunnel gélification op1260(10st4)',
    'T° tunnel pré-chauffage op1260',
    'température tunnel de maintien op1260',
    'T° réservoir résine op1260',
    '1260_T° Lampe IR 1', '1260_T° Lampe IR 2',
    '1260_T° Lampe IR 3',
    'Poids résine piece sortie op1260',
    'N° Série',
    'COMPTEUR PIECE DANS PINCE op1260'
]

DF = pd.DataFrame(np.arange(1, 13).reshape(1, 12),
                  columns=COLUMN_NAMES)

name_cleaner = CleanNames(DF)

def test_clean_one_name():
    new_name = name_cleaner.clean_one_name('T° tunnel gélification op1260(10st4)')
    assert new_name == 't_tunnel_gelification_op1260_10st4'

def test_clean_names():
    # re search returns None if one letter not in pattern
    clean_pattern = re.compile("[a-z0-9_]+")
    cleaned_names = name_cleaner.clean_names(DF)
    for name in cleaned_names:
        assert clean_pattern.fullmatch(name) is not None

def test_matching_dict():
    assert type(name_cleaner.old_new_match) == dict
    assert len(name_cleaner.old_new_match) == DF.shape[1]
