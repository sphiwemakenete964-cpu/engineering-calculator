import pytest

from power_calculator import (
    calculate_power_vi,
    calculate_power_ir,
    calculate_power_vr
)


def test_power_using_voltage_and_current():
    assert calculate_power_vi(12, 2) == 24


def test_power_using_current_and_resistance():
    assert calculate_power_ir(3, 4) == 36


def test_power_using_voltage_and_resistance():
    assert calculate_power_vr(12, 4) == 36


def test_zero_resistance():
    with pytest.raises(ValueError):
        calculate_power_vr(12, 0)