NORMAL = "NORMAL"
WARNING = "WARNING"
CRITICAL = "CRITICAL"

def calculate_battery_power(voltage, current):
    """Calculate battery power in kilowatts."""
    return (voltage * current) / 1000

def evaluate_temperature(temperature):
    """Evaluate battery temperature and return status."""
    if temperature < 45:
        return NORMAL
    elif temperature <= 60:
        return WARNING
    else:
        return CRITICAL