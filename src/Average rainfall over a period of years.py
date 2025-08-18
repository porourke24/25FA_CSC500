# years: keep asking until valid
while True:
    try:
        years = int(input("Enter the number of years: "))
        if years <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a whole number (e.g., 1, 2, 3).")

total_rainfall = 0.0
total_months = 0

for year in range(1, years + 1):
    print(f"\nYear {year}")
    for month in range(1, 12 + 1):
        while True:
            text = input(f"Enter rainfall for month {month} (in inches): ").strip()
            try:
                rainfall = float(text)
                if rainfall < 0:
                    print("Rainfall cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a numeric value (e.g., 2, 3.5, 0).")
        total_rainfall += rainfall
        total_months += 1

average_rainfall = total_rainfall / total_months
print("\nRainfall Summary:")
print(f"Total months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
