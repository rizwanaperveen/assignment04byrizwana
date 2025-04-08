# Dictionary of gravity factors relative to Earth
planet_gravity = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Mars": 0.378,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Earth":1.0,
    "Uranus": 0.92,
    "Neptune": 1.19
}

# Prompt the user to enter their weight on Earth
earth_weight = float(input("Enter your weight on Earth (in kg): "))

# Show planet options
print("\nChoose a planet:")
for planet in planet_gravity:
    print(f"- {planet}")

# Get user choice
chosen_planet = input("\nEnter the name of the planet: ").capitalize()

# Calculate and display weight
if chosen_planet in planet_gravity:
    new_weight = earth_weight * planet_gravity[chosen_planet]
    print(f"\nYour weight on {chosen_planet} would be: {new_weight:.2f} kg")
else:
    print("\nInvalid planet name. Please enter a valid planet from the list.")
