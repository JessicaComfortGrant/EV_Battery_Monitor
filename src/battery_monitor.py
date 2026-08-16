from enum import Enum

from src.logger import setup_logger

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
    if voltage < 300:
        return Status.LOW
    elif voltage <= 450:
        return Status.NORMAL
    else:
        return Status.HIGH

def evaluate_current(current):
    """Evaluate current and return status."""

    if current < 25:
        return Status.LOW
    elif current <= 50:
        return Status.NORMAL
    else:
        return Status.HIGH   


def evaluate_soc(soc):
    """Evaluate state of charge and return status."""

    if soc < 20:
        return Status.LOW
    elif soc <= 80:
        return Status.NORMAL
    else:
        return Status.HIGH


def evaluate_temperature(temperature):
    """Evaluate battery temperature and return status."""
    if temperature < 45:
        return Status.NORMAL
    elif temperature <= 60:
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
 

def monitor_battery(voltage, current, temperature, soc):
    """Monitor battery electrical and thermal conditions."""

    power = calculate_battery_power(voltage, current)
    voltage_status = evaluate_voltage(voltage)
    current_status = evaluate_current(current)
    soc_status = evaluate_soc(soc)
    temperature_status = evaluate_temperature(temperature)
    
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
        "voltage": voltage,
        "voltage_status": voltage_status,
        
        "current": current,
        "current_status": current_status,
        
        "power": power,
        
        "temperature": temperature,
        "temperature_status": temperature_status,
        
        "soc": soc,
        "soc_status": soc_status,
        
        "battery_status": battery_status,
    }