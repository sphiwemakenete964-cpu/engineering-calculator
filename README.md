# Engineering Calculator

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Tests](https://github.com/sphiwemakenete964-cpu/engineering-calculator/actions/workflows/tests.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-green)

A Python-based engineering calculator designed to perform electrical engineering calculations through a simple menu-driven interface.

This project demonstrates modular programming, numerical calculations, input validation and automated software testing.

## Features

### 1. Ohm's Law Calculator

Calculate voltage, current or resistance when the other two quantities are known.

The calculator uses:

$
V=IR
$

| Symbol | Quantity | Unit |
|---|---|---|
| V | Voltage | Volts (V) |
| I | Current | Amperes (A) |
| R | Resistance | Ohms (Ω) |

### 2. Electrical Power Calculator

Calculate electrical power using different combinations of voltage, current and resistance.

The implemented equations are:

- $P = VI$
- $P = I^2R$
- $P = \frac{V^2}{R}$

### 3. Voltage Divider Calculator

Calculate the output voltage of a two-resistor voltage divider.

$$
V_{out} = V_{in}\frac{R_2}{R_1+R_2}
$$

## Technologies

- Python 3
- Pytest – automated testing
- Git and GitHub – version control
- GitHub Actions – continuous integration

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sphiwemakenete964-cpu/engineering-calculator.git
```

2. Navigate into the project directory:

```bash
cd engineering-calculator
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Launch the main application:

```bash
python main.py
```

The application provides a menu for selecting the available engineering calculators.

## Running Automated Tests

This project uses Pytest to verify the calculation functions and handle invalid inputs.

Run the complete test suite:

```bash
python -m pytest -p no:cacheprovider
```

The tests cover:

- Ohm's Law calculations
- Electrical power calculations
- Voltage divider calculations
- Invalid input and zero-resistance conditions

## Continuous Integration

GitHub Actions automatically runs the automated test suite when code is pushed to the configured branches or when a Pull Request targeting `main` is opened.

This helps identify errors before changes are merged into the main branch.

## Project Structure

```text
engineering-calculator/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── main.py
├── ohms_law.py
├── power_calculator.py
├── voltage_divider.py
│
├── test_ohms_law.py
├── test_power_calculator.py
├── test_voltage_divider.py
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Future Improvements

- Series and parallel resistance calculator
- RC time constant calculator
- Capacitor calculations
- More comprehensive test coverage
- Improved user interface

## Purpose

This project is part of my journey in developing practical programming and engineering skills.

As a Mechatronics Engineering student, I am interested in combining software development with electrical engineering principles to build useful engineering tools.

The project is continuously evolving as I explore more advanced programming techniques and engineering applications.

---

**Created by Sphiwe**

Mechatronics Engineering | University of Cape Town