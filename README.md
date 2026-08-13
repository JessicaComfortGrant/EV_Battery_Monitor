# EV Battery Monitor

A Python-based battery monitoring system for evaluating Electric Vehicle (EV) battery
operating conditions using voltage, current, temperature, and
state of charge (SOC).

## Overview

The EV Battery Monitor evaluates battery measurements against defined
operating thresholds and classifies the battery condition as:

- NORMAL
- WARNING
- CRITICAL

The project demonstrates modular Python development, input validation,
automated testing, integration testing, and logging.

## Features

- Battery voltage monitoring
- Battery current monitoring
- Temperature monitoring
- State-of-Charge (SOC) monitoring
- Battery power calculation
- Overall battery-status determination
- CLI input validation
- Operational logging
- Automated unit and integration testing

## Architecture

```text
User Input
    ↓
CLI & Validation
    ↓
Battery Monitor
    ↓
┌──────────┬──────────┬─────────────┬─────┐
│ Voltage  │ Current  │ Temperature │ SOC │
└──────────┴──────────┴─────────────┴─────┘
    ↓
Battery Status
    ↓
Output + Logging
```

## Installation

### Clone the repository

```bash
git clone https://github.com/JessicaComfortGrant/EV_Battery_Monitor.git
cd EV_Battery_Monitor
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the command-line interface:

```bash
python src/cli.py
```

The application prompts the user to enter:

- Battery voltage
- Battery current
- Battery temperature
- State of Charge (SOC)

The system evaluates the measurements and returns the overall
battery condition.

## Testing

Run the complete test suite with:

```bash
python -m unittest discover -s tests -v
```

The test suite covers:

- Battery power calculation
- Voltage evaluation
- Current evaluation
- Temperature evaluation
- SOC evaluation
- Battery-status determination
- Battery monitoring workflow
- CLI input validation
- End-to-end behaviour
- Integration scenarios
- Logging

### Test Status

**60 tests passing**

```text
Ran 60 tests
OK
```

## Project Structure

```text
EV_Battery_Monitor/
│
├── data/
│
├── src/
│   ├── battery_monitor.py
│   ├── cli.py
│   └── logger.py
│
├── tests/
│   ├── test_battery_monitor.py
│   ├── test_cli.py
│   ├── test_e2e.py
│   ├── test_integration.py
│   └── test_logger.py
│
├── .gitignore
├── battery_monitor.log
├── README.md
└── requirements.txt
```

## Technology

- **Python** — Application development
- **unittest** — Automated testing
- **logging** — Application logging
- **Git** — Version control
- **GitHub** — Repository management

## Battery Monitoring

The system evaluates four primary battery parameters:

| Parameter | Unit | Purpose |
|---|---|---|
| Voltage | V | Evaluates battery voltage condition |
| Current | A | Evaluates battery current condition |
| Temperature | °C | Evaluates battery thermal condition |
| State of Charge | % | Evaluates remaining battery charge |

Battery power is calculated using:

```text
Power = Voltage × Current
```

The individual parameter evaluations are combined to determine the
overall battery condition.

## Status Classification

The system uses three battery-status levels:

| Status | Meaning |
|---|---|
| `NORMAL` | Battery parameters are operating within the defined normal range |
| `WARNING` | One or more parameters require attention |
| `CRITICAL` | One or more parameters have reached a critical condition |

The thresholds used by the application are project-defined monitoring
thresholds and are not intended to represent universal EV battery
safety limits.

## Logging

The application uses Python's built-in `logging` module to record
battery monitoring events.

The monitoring log is written to:

```text
battery_monitor.log
```

Logging provides visibility into battery conditions and supports
debugging and future monitoring functionality.

## Limitations

This is a **V1 software-based battery monitoring system**.

The current implementation does not include:

- Real EV battery hardware
- CAN bus communication
- ECU integration
- Physical battery sensors
- Real-time vehicle telemetry
- Persistent time-series data storage
- Machine-learning-based prediction

The current system operates on user-provided battery measurements.

## Future Development

Future versions may extend the system with:

- Real-time battery data acquisition
- CAN bus integration
- EV sensor and ECU integration
- Battery data storage
- Data visualization
- Battery anomaly detection
- State-of-Health (SOH) estimation
- Remaining Useful Life (RUL) prediction
- Machine-learning-based battery prediction
- Energy optimization for electric mobility

## Project Direction

The EV Battery Monitor provides a foundation for future work at the
intersection of:

- Data Science
- Machine Learning
- Electric Vehicle Systems
- Battery Intelligence
- Intelligent Transportation Systems

The long-term direction is to evolve the system from rule-based
battery monitoring toward data-driven and machine-learning-enabled
EV intelligence.

## Author

**Jessica Comfort Grant**

Data Scientist focused on machine learning, intelligent systems,
electric mobility, and data-driven engineering.
