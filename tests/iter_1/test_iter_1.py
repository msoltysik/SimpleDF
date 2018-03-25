import pytest

from tests.conftest import DATA_FRAMES


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_initialize_empty_df(df):
    # GIVEN
    size = 0

    # WHEN
    df = df()

    # THEN
    assert df is not None
    assert df.size == size


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_init_by_dict_df(df, dataset_1):
    # GIVEN
    data = dataset_1
    expected_keys = ['A', 'B', 'C', 'D']
    expected_values = [
        [1., '44', True, 4],
        [1., '44', True, 3],
        [1., '44', True, 2],
        [1., '44', True, 1],
        [1., '44', True, 4],
    ]

    # WHEN
    df = df(data=data)

    # THEN
    assert list(df.keys()) == expected_keys
    for idx, val in enumerate(df.values):
        assert list(val) == expected_values[idx]
