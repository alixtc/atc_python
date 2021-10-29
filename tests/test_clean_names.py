from atc_python.clean_names import clean_names, clean_one_name
import pandas as pd
import numpy as np
import re

def test_clean_one_name():
    new_name = clean_one_name('T° tunnel gélification op1260(10st4)')
    assert new_name == 't_tunnel_gelification_op1260_10st4'


COLUMN_NAMES = [
    'Carton Rouge_op1260', 'température four cuissonop1260',
    'T° tunnel gélification op1260(10st4)', 'T° tunnel pré-chauffage op1260',
    'température tunnel de maintien op1260', 'T° réservoir résine op1260',
    '1260_T° Lampe IR 1', '1260_T° Lampe IR 2', '1260_T° Lampe IR 3',
    'Poids résine piece sortie op1260', 'N° Série',
    'COMPTEUR PIECE DANS PINCE op1260'
]

DF = pd.DataFrame(np.arange(1, 13).reshape(1, 12),
             columns=COLUMN_NAMES)


def test_clean_names():
    # re search returns None if one letter not in pattern
    clean_pattern = re.compile("[a-z0-9_]+")
    cleaned_names = clean_names(DF)
    for name in cleaned_names:
        assert clean_pattern.fullmatch(name) is not None
