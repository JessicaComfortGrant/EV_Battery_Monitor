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
        return LOW
    elif voltage <= 450:
        return NORMAL
    else:
        return HIGH

def evaluate_temperature(temperature):
    """Evaluate battery temperature and return status."""
    if temperature < 45:
        return NORMAL
    elif temperature <= 60:
        return WARNING
    else:
        return CRITICAL
    
def determine_battery_status(temperature_status):
     """Determine overall battery status."""
     return temperature_status
 

def monitor_battery(voltage, current, temperature):
    """Monitor battery electrical and thermal conditions."""

    power = calculate_battery_power(voltage, current)
    temperature_status = evaluate_temperature(temperature)
    voltage_status = evaluate_voltage(voltage)
    battery_status = determine_battery_status(temperature_status)

    return {
        "voltage": voltage,
        "current": current,
        "temperature": temperature,
        "power": power,
        "voltage_status": voltage_status,
        "temperature_status": temperature_status,
        "battery_status": battery_status,
    }