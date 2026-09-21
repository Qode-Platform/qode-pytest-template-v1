"""Fixtures shared by the whole suite."""

import pytest


@pytest.fixture
def sample_values() -> list[float]:
    return [1.0, 2.0, 3.5]


@pytest.fixture
def tmp_config(tmp_path):
    path = tmp_path / "config.ini"
    path.write_text("[app]\nmode = test\n")
    return path
