from src.battery_monitor import monitor_battery

def get_float_input(prompt):
    """Get a valid floating-point number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number")
            

def display_result(result):
    """Display the battery monitoring result."""
    
    print("\n" + "-" * 40)
    print("BATTERY MONITORING RESULT")
    print("-" * 40)
    
    print(f"Voltage: {result['voltage']:.2f} V")
    print(f"Current: {result['current']:.2f} A")
    print(f"Power: {result['power']:.2f} kW")
    print(f"Temperature: {result['temperature']:.2f} °C")
    
    print(f"\nTemperature Status:  {result['temperature_status']}")
    print(f"Battery Status:      {result['battery_status']}")

def main():
    """Run the EV Battery Monitor CLI."""
    
    print("=" * 40 )
    print("       EV BATTERY MONITOR")
    print("=" * 40 )
    
    voltage = get_float_input("Enter battery voltage (V): ")
    current = get_float_input("Enter battery current (A): ")
    temperature = get_float_input("Enter battery temperature (°C): ")

    result = monitor_battery(
        voltage, 
        current, 
        temperature
    )
    
    display_result(result)

if __name__ == "__main__":
    main()