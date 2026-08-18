from datetime import datetime

from src.battery_reading import BatteryReading
from src.battery_monitor import monitor_battery

def get_float_input(prompt, minimum=None, maximum=None):
    """Get a valid floating-point number from the user."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        
        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}. Please try again.")
            continue
        
        if maximum is not None and value > maximum:
            print(f"Value must be at most {maximum}. Please try again.")
            continue
        
        return value
            

def display_result(result):
    """Display the battery monitoring result."""
    
    print("\n" + "-" * 40)
    print("BATTERY MONITORING RESULT")
    print("-" * 40)
    
    print(f"Timestamp:            {result['timestamp']}")
    
    print(f"\nVoltage:             {result['voltage']:.2f} V")
    print(f"Voltage Status:      {result['voltage_status'].value}")

    print(f"\nCurrent:             {result['current']:.2f} A")
    print(f"Current Status:      {result['current_status'].value}")
    
    print(f"\nPower:               {result['power']:.2f} kW")

    print(f"\nTemperature:         {result['temperature']:.2f} °C")
    print(f"Temperature Status:  {result['temperature_status'].value}")
    
    print(f"\nState of Charge:     {result['soc']:.2f} %")
    print(f"SOC Status:          {result['soc_status'].value}")
    
    print("\n" + "-" * 40)
    print(f"Battery Status:      {result['battery_status'].value}")
    print("-" * 40)

def main():
    """Run the EV Battery Monitor CLI."""
    
    print("=" * 40 )
    print("       EV BATTERY MONITOR")
    print("=" * 40 )
    
    print("\nEnter the following battery parameters:")
    print("-" * 40 )
    
    voltage = get_float_input(
        "Enter battery voltage (V): ",
        minimum=0.0
    )
    
    
    current = get_float_input(
        "Enter battery current (A): "
    )
    
    
    temperature = get_float_input(
        "Enter battery temperature (°C): ",
        minimum=-40,
        maximum=100
    )
    
    soc = get_float_input(
        "Enter battery state of charge (%): ",
        minimum=0.0,
        maximum=100.0
        )

    reading = BatteryReading(
        voltage=voltage,
        current=current,
        temperature=temperature,
        soc=soc,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    result = monitor_battery(reading)

    
    display_result(result)

if __name__ == "__main__":
    main()