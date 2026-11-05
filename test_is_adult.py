import pytest

from is_adult import is_adult


def test_is_adult_returns_false_for_age_17():
    assert is_adult(17) is False


def test_is_adult_returns_true_for_age_18():
    assert is_adult(18) is True


def test_is_adult_raises_for_negative_age():
    with pytest.raises(ValueError):
        is_adult(-1)
