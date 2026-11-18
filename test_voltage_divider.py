import pytest

from voltage_divider import calculate_voltage_divider


def test_voltage_divider_basic():
    result = calculate_voltage_divider(12, 1000, 2000)
    assert result == pytest.approx(8.0)


def test_voltage_divider_equal_resistors():
    result = calculate_voltage_divider(9, 1000, 1000)
    assert result == pytest.approx(4.5)


def test_voltage_divider_zero_resistance():
    with pytest.raises(ValueError):
        calculate_voltage_divider(12, 0, 0)