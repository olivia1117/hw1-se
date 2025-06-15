'''
Title: Fermat's Near Miss Calculator  

External Files: N/A

External Files List: N/A

Programmers: Olivia Adamic and Alejandrina Pareja

Email Addresses: oliviaradamic@lewisu.edu, AlejandrinaPareja@lewisu.edu

Course: SU25-CPSC-60500-001

Date Finished: 2025-06-15

Description: This program helps users calculate near misses for 
Fermat's Last Theorem for given values of x, y, n, and k. 
It searches for combinations where x^n + y^n is close to z^n, 
and reports the smallest relative miss. The user is prompted for a 
value of n that fits: 2 < n <12, and a value of k that 
fits: 10 <= x <= k, and where 10 <= y <= k. The program 
systematically searches for the closest near miss, reporting each 
new best found.

Resources Used: N/A

'''

import math

# this function asks for user input, searches for near misses, and shows the results
def main():
    print("Welcome to Fermat's Near Miss Calculator!")

    # Prompt for n with input validation, if the user enters a value outside the constraints, 
    # then the program will ask for a valid input again 
    while True:
        try:
            n = int(input("Enter the value of n (2 < n < 12): "))
            if 2 < n < 12:
                break
            else:
                print("Enter an integer greater than 2 and less than 12 only, please.")
        except ValueError:
            print("Invalid input. Enter integer only.")

    # Prompt for k with input validation, if the user enters a value outside the constraints, 
    # it will ask for a valid input again
    while True:
        try:
            k = int(input("Enter the value of k (10 <= x, y <= k): "))
            if k > 10:
                break
            else:
                print("Enter integer greater than 10.")
        except ValueError:
            print("Invalid input. Please enter integer.")

    top_missed = float('inf')  # Smallest relative miss found so far
    top_combo = None           # Store the best (x, y, z, difference, error_ratio)

    # Loop through all x, y combinations in the specified range
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            if x == y:
                continue  # Skip cases where x == y to avoid duplicates

            total = x ** n + y ** n  # Calculate x^n + y^n
            z = int(total ** (1 / n))  # Approximate the nth root to find z

            below_power = z ** n
            above_power = (z + 1) ** n

            # Find which z^n or (z+1)^n is closer to total
            difference = min(abs(total - below_power), abs(above_power - total))
            error_ratio = difference / total

            # If this is the smallest miss so far, print and store it
            if error_ratio < top_missed:
                top_missed = error_ratio
                top_combo = (x, y, z, difference, error_ratio)

                print()
                print("New top miss found:")
                print(f"  x = {x}, y = {y}, z = {z}")
                print(f"  Difference = {difference}")
                print(f"  Relative miss = {error_ratio:.10f} ({error_ratio:.6%})\n")

    # Print the smallest miss found at the end
    if top_combo:
        x, y, z, difference, error_ratio = top_combo
        print()
        print("Search Finished:")
        print(f"Smallest near miss found for n = {n}, k = {k}:")
        print(f"  x = {x}, y = {y}, z = {z}")
        print(f"  Difference = {difference}")
        print(f"  Relative miss = {error_ratio:.10f} ({error_ratio:.6%})")
        print()

    input("\nPress Enter to exit...")

main()








