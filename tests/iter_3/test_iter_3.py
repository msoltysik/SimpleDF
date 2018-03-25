import pytest

from tests.conftest import DATA_FRAMES


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_empty_dfs_equals(df):
    # GIVEN

    # WHEN
    df1 = df()
    df2 = df()

    # THEN
    assert df1.equals(df2)
    assert df2.equals(df1)


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_dfs_equals(df, dataset_1):
    # GIVEN

    # WHEN
    df1 = df(dataset_1)
    df2 = df(dataset_1)

    # THEN
    assert df1.equals(df2)
    assert df2.equals(df1)


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_dfs_greater_than(df, dataset_1):
    # GIVEN

    # WHEN
    df = df(dataset_1)

    # THEN

    assert list(df.D > 4) == [False, False, False, False, False]
    assert list(df.D >= 2) == [True, True, True, False, True]


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_dfs_equals(df, dataset_1):
    # GIVEN
    ex_values = [
        [1., '44', True, 4],
        [1., '44', True, 3],
        [1., '44', True, 4]
    ]

    # WHEN
    df = df(dataset_1)

    # THEN
    values = df[df.D > 2].values
    assert len(values) == 3
    for i in range(len(values)):
        assert list(values[i]) == ex_values[i]
