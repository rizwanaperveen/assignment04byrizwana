SPEED_OF_LIGHT: int = 299_792_458  # Speed of light in meters per second (m/s)

def einstien() -> None:
    try:
        mass_kg: float = float(input("Enter mass in kilograms: "))
        energy_joules: float = mass_kg * (SPEED_OF_LIGHT ** 2)

        print("\nCalculating energy using E = m * c²...")
        print(f"Mass (m): {mass_kg} kg")
        print(f"Speed of Light (c): {SPEED_OF_LIGHT} m/s")
        print(f"Energy (E): {energy_joules:.2e} joules")

    except ValueError:
        print("Please enter a valid number for mass.")

if __name__ == "__main__":
    einstien()
