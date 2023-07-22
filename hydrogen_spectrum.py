#!/usr/bin/env python3
"""hydrogen_spectrum.py"""

# This code calculates and displays the wavelengths (in nanometers) for both the Pfund 
# and Humphreys high energy spectral series of Hydrogen using both 
# the Rydberg and Bohr formulas. 
# Code for the Rydberg and Bohr formulas is copied from that given by 
# Dr. David Biersach in spectrum_bohr.py and spectrum_rydberg.py.

# Code was also aided by:https://en.wikipedia.org/wiki/Hydrogen_spectral_series#Pfund_series_(n′_=_5) 
# and solutions provided by Dr. David Biersach. 

def spectrum_calculations(series_number: int) -> None:
    """Calculate wavelengths using Bohr and Rydberg formulas"""
    # Defining the Bohr formula
    # 𝐸_𝑛=−𝐸_0/𝑛^2  where 𝐸_0=(𝑒^4 𝑚)/(8𝜀_0^2 ℎ^2 )

    # Define the constants as integers first:

    # 𝑒=1.602×10^(−19) 𝐶
    e_charge: float = 1.602e-19

    # 𝑚=9.109×10^(−31) 𝑘𝑔
    e_mass: float = 9.109e-31

    # 𝜀_0=8.854×10^(−12) 𝐶^2/𝑁𝑚^2
    permittivity: float = 8.854e-12

    # Planck's constant ℎ=6.626×10^(−34) 𝐽𝑠𝑒𝑐
    h_plank: float = 6.626e-34

    # Speed of light 𝑐=2.998×10^8 𝑚/𝑠𝑒𝑐
    speed_light: float = 2.998e8

    # Bohr's formula for ground state energy
    # Define 𝐸_0=(𝑒^4 𝑚)/(8𝜀_0^2 ℎ^2 )
    e_0: float = (pow(e_charge, 4) * e_mass) / (
        8 * pow(permittivity, 2) * pow(h_plank, 2)
    )


    # Define Rydberg's constant 
    rydberg_constant: float = 1.0967757e7

    # The final orbit is equal to either the Pfund or Humphreys series number.
    final_orbit: int = series_number

    # Initialize the table headings
    print (
            ("Series  "
            "Initial  Final  "
            "Rydberg  "
            "Bohr "
            )
        )
    # Print a space between headings and values
    print()
    for init_orbit in range(final_orbit + 1, final_orbit + 6):
        # 𝐸_𝑛=−𝐸_0/𝑛^2 
        # Initial energy level
        e_i: float = -e_0 / pow(init_orbit, 2)
        # Final energy level
        e_f: float = -e_0 / pow(final_orbit, 2)
        # Bohr's formula for waveLength in nanometers
        # From Einstein:𝜆=ℎ𝑐/(𝐸_𝑖𝑛𝑖𝑡𝑖𝑎𝑙−𝐸_𝑓𝑖𝑛𝑎𝑙 )
        wave_length_bohr: float = h_plank * speed_light / (e_i - e_f) * 1e9

        # Rydberg's formula for waveLength in nanometers
        # 1e9 to print out in nm
        wave_length_rydberg: float = (
            1 / (rydberg_constant * (1 / pow(final_orbit, 2) - 1 / pow(init_orbit, 2))) * 1e9
        )
        # Print the table values for the Pfund series
        if final_orbit== 5: 
            print (
            ("Pfund "
            f"{init_orbit:>2} ---> {final_orbit:>2}  "
            f"{wave_length_rydberg:8.0f}nm"
            f"{wave_length_bohr:8.0f}nm"
            )
        )
        # Print the table values for the Humphreys series 
        else: 
            print (
            ("Humphreys "
            f"{init_orbit:>2} ---> {final_orbit:>2}  "
            f"{wave_length_rydberg:8.0f}nm"
            f"{wave_length_bohr:8.0f}nm"
            )
        )

    # prints a blank line in between each initial_orbit value 
    print()

def main() -> None:
    """Defining the entry point for the function"""

    # Define the Pfund series integer n′ = 5
    pfund: int = 5 

    # Define the Humphreys series integer n′ = 6
    humphreys: int = 6

    #Initialize the series_number integer
    series_number: int = 0 

    # Calculate and display the wavelengths for Pfund series 
    # using both the Rydberg and Bohr formulas
    series_number= pfund 
    spectrum_calculations(series_number)
  
    # Print a blank space 
    print ()
    # Calculate and display the wavelengths for Humphreys series 
    # using both the Rydberg and Bohr formulas
    series_number = humphreys
    spectrum_calculations(series_number)
   

if __name__ == "__main__":
    # Call the main function 
    main()

