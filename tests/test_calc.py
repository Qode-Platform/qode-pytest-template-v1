import pytest

from mypkg import divide, running_total


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [(6, 3, 2.0), (-6, 3, -2.0), (1, 8, 0.125)],
)
def test_divide(numerator, denominator, expected):
    assert divide(numerator, denominator) == expected


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="non-zero"):
        divide(1, 0)


def test_running_total(sample_values):
    assert running_total(sample_values) == [1.0, 3.0, 6.5]


def test_fixture_writes_tmp_file(tmp_config):
    assert "mode = test" in tmp_config.read_text()


@pytest.mark.slow
def test_marked_slow():
    assert sum(range(100_000)) > 0
