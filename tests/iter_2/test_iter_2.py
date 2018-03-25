import pytest

from tests.conftest import DATA_FRAMES


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_get_value_using_getter(df, dataset_1):
    # GIVEN
    data = dataset_1
    df_a = [1., 1., 1., 1., 1.]
    df_b = ['44', '44', '44', '44', '44']
    df_c = [True, True, True, True, True]
    df_d = [4, 3, 2, 1, 4]

    # WHEN
    df = df(data)

    # THEN
    assert list(df.A) == df_a
    assert list(df.B) == df_b
    assert list(df.C) == df_c
    assert list(df.D) == df_d


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_get_value_using_brackets(df, dataset_1):
    # GIVEN
    data = dataset_1
    df_a = [1., 1., 1., 1., 1.]
    df_b = ['44', '44', '44', '44', '44']
    df_c = [True, True, True, True, True]
    df_d = [4, 3, 2, 1, 4]

    # WHEN
    df = df(data)

    # THEN
    assert list(df['A']) == df_a
    assert list(df['B']) == df_b
    assert list(df['C']) == df_c
    assert list(df['D']) == df_d


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_get_missing_value_by_getter(df):
    # GIVEN
    data = {'A': 1., 'B': '44', 'C': True, 'D': [4, 3, 2, 1, 4]}
    missing_key = 'XxXxXx'
    err = AttributeError
    err_msg = f"'DataFrame' object has no attribute '{missing_key}'"

    # WHEN
    df = df(data)

    # THEN
    assert missing_key not in df.keys()

    with pytest.raises(err) as exc_info:
        assert eval('df.' + missing_key)
    assert exc_info.typename == err.__name__
    assert exc_info.value.args[0] == err_msg


@pytest.mark.parametrize("df", DATA_FRAMES)
def test_get_missing_value_by_brackets(df):
    # GIVEN
    data = {'A': 1., 'B': '44', 'C': True, 'D': [4, 3, 2, 1, 4]}
    missing_key = 'XxXxXx'
    err = KeyError

    # WHEN
    df = df(data)

    # THEN
    assert missing_key not in df.keys()

    with pytest.raises(err) as exc_info:
        assert df[missing_key]
    assert exc_info.typename == err.__name__
    assert exc_info.value.args[0] == missing_key
