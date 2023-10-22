import time

# Initial variables
solar_energy_collected = 0
water_temperature = 20  # Initial water temperature in degrees Celsius
water_level = 0.5  # Initial water level in the upper reservoir (0-1)

# Main simulation loop
while water_temperature < 300:
    # Simulate solar energy collection (increase yellow color intensity)
    solar_energy_collected += 1
    solar_energy_collected = min(solar_energy_collected, 255)

    # Simulate steam generation (based on solar energy collected)
    water_temperature += 0.01 * solar_energy_collected

    # Simulate electricity generation (increase blue color intensity)
    electricity_generated = max(water_temperature - 50, 0)

    # Simulate upper reservoir filling
    water_level = min(water_level + 0.001, 1)

    # Clear the console
    print("\033c")  # Clear the console for a smoother animation (Linux/Unix)
    # On Windows, you can use 'cls' instead of '\033c'

    # Display the simulated elements
    print(f"Solar Energy: {'█' * int(solar_energy_collected // 5)}")
    print(f"Water Temperature: {water_temperature:.2f}°C")
    print(f"Electricity Generated: {'█' * int(electricity_generated // 10)}")
    print(f"Upper Reservoir: {'█' * int(water_level * 50)}")
    print(f"Lower Reservoir: {'█' * int((1 - water_level) * 50)}")

    # Wait for a short time to control the animation speed
    time.sleep(0.1)
