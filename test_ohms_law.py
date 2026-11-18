import pytest

from ohms_law import (
    calculate_voltage,
    calculate_current,
    calculate_resistance
)


def test_calculate_voltage():
    assert calculate_voltage(2, 10) == 20


def test_calculate_current():
    assert calculate_current(12, 4) == 3


def test_calculate_resistance():
    assert calculate_resistance(9, 0.5) == 18


def test_zero_resistance():
    with pytest.raises(ValueError):
        calculate_current(12, 0)


def test_zero_current():
    with pytest.raises(ValueError):
        calculate_resistance(9, 0)