import time

# Initial variables
water_level = 0.5  # Initial water level in the upper reservoir (0-1)
total_energy_generated = 0  # Initialize total energy generated

# Main simulation loop
print("When water is flowing from upper reservoir to lower reservoir")
while water_level > 0.05:
    # Simulate water flow from upper to lower reservoir
    water_transfer_rate = 0.01  # Rate of water transfer from upper to lower reservoir

    # Calculate the amount of water to transfer
    water_transfer = water_level * water_transfer_rate

    # Update water levels in the reservoirs
    water_level -= water_transfer

    # Simulate electricity generation (increase blue color intensity)
    electricity_generated = water_transfer_rate * 100  # Simplified electricity generation

    # Add the current electricity generated to the total energy
    total_energy_generated += electricity_generated

    # Clear the console
    print("\033c")  # Clear the console for a smoother animation (Linux/Unix)
    # On Windows, you can use 'cls' instead of '\033c'

    # Display the simulated elements
    print(f"Electricity Generated: {'█' * int(electricity_generated // 10)}")
    print(f"Upper Reservoir: {'█' * int(water_level * 50)}")
    print(f"Lower Reservoir: {'█' * int((1 - water_level) * 50)}")
    print(f"Total Energy Generated: {total_energy_generated} kW")

    # Wait for a short time to control the animation speed
    time.sleep(0.1)
