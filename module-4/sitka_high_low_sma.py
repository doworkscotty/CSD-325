#Scott Anderson Module 4.2 Assignment: High/Low Temperatures


import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

def read_weather_data(filename):
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                print(f"Missing data for {row[2]}")
                continue
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows

def plot_temperatures(dates, temps, label, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    plt.title(f"Daily {label} Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = read_weather_data(filename)

    while True:
        print("\nWelcome to Sitka Weather Viewer")
        print("Choose an option:")
        print("1. High Temperatures")
        print("2. Low Temperatures")
        print("3. Exit")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == '1':
            plot_temperatures(dates, highs, "High", "red")
        elif choice == '2':
            plot_temperatures(dates, lows, "Low", "blue")
        elif choice == '3':
            print("Thank you for using Sitka Weather Viewer. Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
