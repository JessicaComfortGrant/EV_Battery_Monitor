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
    
    voltage = get_float_input(
        "Enter battery voltage (V): ",
        minimum=0.0
    )
    
    
    current = get_float_input(
        "Enter battery current (A): ",
        minimum=0.0
    )
    
    
    temperature = get_float_input(
        "Enter battery temperature (°C): ",
        minimum=-40,
        maximum=100
    )

    result = monitor_battery(
        voltage, 
        current, 
        temperature
    )
    
    display_result(result)

if __name__ == "__main__":
    main()