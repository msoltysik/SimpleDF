import pandas
import pytest

import simple_df

only_pandas = True
DATA_FRAMES = [pandas.DataFrame] if only_pandas else [pandas.DataFrame, simple_df.SimpleDataFrame]


def transform_nan_to_str(val):
    return str(val) if (type(val) == float and str(val) == 'nan') else val


@pytest.fixture
def dataset_1():
    return {
        'A': 1.,
        'B': '44',
        'C': True,
        'D': [4, 3, 2, 1, 4]
    }


@pytest.fixture
def dataset_2():
    return {
        'B': [10, 20, 30, 40, 50],
        'E': 88
    }

