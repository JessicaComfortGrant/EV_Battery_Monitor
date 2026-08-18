from enum import Enum

from src.battery_reading import BatteryReading
from src.logger import setup_logger
from src.thresholds import (
    VOLTAGE_MIN,
    VOLTAGE_MAX,
    CURRENT_MIN,
    CURRENT_MAX,
    SOC_MIN,
    SOC_MAX,
    TEMPERATURE_WARNING,
    TEMPERATURE_CRITICAL
)

logger = setup_logger()

class Status(Enum):
    """Enum for battery status levels."""
    HIGH = "HIGH"
    LOW = "LOW"
    NORMAL = "NORMAL"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

def calculate_battery_power(voltage, current):
    """Calculate battery power in kilowatts."""
    return (voltage * current) / 1000

def evaluate_voltage(voltage):
    """Evaluate battery voltage and return status."""
    if voltage < VOLTAGE_MIN:
        return Status.LOW
    elif voltage <= VOLTAGE_MAX:
        return Status.NORMAL
    else:
        return Status.HIGH

def evaluate_current(current):
    """Evaluate current and return status."""

    if current < CURRENT_MIN:
        return Status.LOW
    elif current <= CURRENT_MAX:
        return Status.NORMAL
    else:
        return Status.HIGH   


def evaluate_soc(soc):
    """Evaluate state of charge and return status."""

    if soc < SOC_MIN:
        return Status.LOW
    elif soc <= SOC_MAX:
        return Status.NORMAL
    else:
        return Status.HIGH


def evaluate_temperature(temperature):
    """Evaluate battery temperature and return status."""
    if temperature < TEMPERATURE_WARNING:
        return Status.NORMAL
    elif temperature <= TEMPERATURE_CRITICAL:
        return Status.WARNING
    else:
        return Status.CRITICAL

def determine_battery_status(
    voltage_status,
    current_status,
    temperature_status,
    soc_status
):
    """Determine overall battery health status."""

    if temperature_status == Status.CRITICAL:
        return Status.CRITICAL

    elif temperature_status == Status.WARNING:
        return Status.WARNING

    else:
        return Status.NORMAL
 

def monitor_battery(reading: BatteryReading):
    """Monitor battery electrical and thermal conditions."""

    power = calculate_battery_power(reading.voltage, reading.current)
    voltage_status = evaluate_voltage(reading.voltage)
    current_status = evaluate_current(reading.current)
    soc_status = evaluate_soc(reading.soc)
    temperature_status = evaluate_temperature(reading.temperature)
    
    battery_status = determine_battery_status(
        voltage_status,
        current_status,
        temperature_status,
        soc_status
    )
    
    if battery_status == Status.CRITICAL:
        logger.critical("Battery status: CRITICAL")
    elif battery_status == Status.WARNING:
        logger.warning("Battery status: WARNING")
    else:
        logger.info("Battery status: NORMAL")

    return {
        "voltage": reading.voltage,
        "voltage_status": voltage_status,
        
        "current": reading.current,
        "current_status": current_status,
        
        "power": power,
        
        "temperature": reading.temperature,
        "temperature_status": temperature_status,
        
        "soc": reading.soc,
        "soc_status": soc_status,
        
        "timestamp": reading.timestamp,
        
        "battery_status": battery_status,
    }