def extrapolate_ppg(ppg, mpg):
    # Return 0 if ppg is 0
    if ppg == 0:
        return 0

    # Calculate extrapolated PPG for 48 minutes
    extrapolated_ppg = (ppg / mpg) * 48

    # Round to the nearest tenth
    return round(extrapolated_ppg, 1)


# Example usage
ppg = float(input("Enter points per game (ppg): "))
mpg = float(input("Enter minutes per game (mpg): "))

extrapolated_points = extrapolate_ppg(ppg, mpg)
print(f"Extrapolated points per 48 minutes: {extrapolated_points}")