import pytest

from tests.conftest import DATA_FRAMES, transform_nan_to_str


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_concat_dfs(df, dataset_1, dataset_2):
    # GIVEN
    exp_values = [
        [1.0, '44', True, 4.0, 'nan'],
        [1.0, '44', True, 3.0, 'nan'],
        [1.0, '44', True, 2.0, 'nan'],
        [1.0, '44', True, 1.0, 'nan'],
        [1.0, '44', True, 4.0, 'nan'],
        ['nan', 10, 'nan', 'nan', 88.0],
        ['nan', 20, 'nan', 'nan', 88.0],
        ['nan', 30, 'nan', 'nan', 88.0],
        ['nan', 40, 'nan', 'nan', 88.0],
        ['nan', 50, 'nan', 'nan', 88.0]
    ]

    # WHEN
    df1 = df(dataset_1)
    df2 = df(dataset_2)

    # THEN
    result = df1.append(df2)
    assert list(result.keys()) == ['A', 'B', 'C', 'D', 'E']
    assert len(result.values) == 10

    for i, val in enumerate(result.values):
        val = list(map(transform_nan_to_str, val))
        assert val == exp_values[i]


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_selection_by_position(df, dataset_1):
    # GIVEN

    # WHEN
    df = df(dataset_1)

    # THEN
    result = df.iloc[1:3]
    assert len(result.values) == 2
    assert list(result.values[0]) == [1.0, '44', True, 3]
    assert list(result.values[1]) == [1.0, '44', True, 2]


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_selection_by_position_location(df, dataset_1):
    # GIVEN
    exp_values = [[1.0, True, 3], [1.0, True, 2], [1.0, True, 4]]

    # WHEN
    df = df(dataset_1)

    # THEN
    result = df.iloc[[1, 2, 4], [0, 2, 3]]
    assert len(result.values) == 3
    for i, val in enumerate(result.values):
        assert list(val) == exp_values[i]
