# Author: Scott Anderson
# Assignment: Module 1 - On the Wall
# Date: 06/07/2025
# Description: Countdown song - "X bottles of beer on the wall"

def countdown_bottles(starting_bottles):
    for bottles in range(starting_bottles, 0, -1):
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            next_bottles = bottles - 1
            bottle_word = "bottle" if next_bottles == 1 else "bottles"
            print(f"Take one down and pass it around, {next_bottles} {bottle_word} of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")

def main():
    try:
        bottles = int(input("Enter number of bottles: "))
        if bottles < 1:
            print("Please enter a number greater than 0.")
        else:
            countdown_bottles(bottles)
            print("Time to go buy more beer!")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

