# Reads a file specified as a command-line argument and processes each line to calculate the sum of two float values.

# Parameters:
# None, since the function expects a file to be provided as a command-line argument

# Behavior:
# The function attempts to open the specified file. For each line in the file:
# It splits the line into two values and converts them to floats then prints their sum.
# If a line doesn't have two values or the values can't be converted to floats, it prints an error message
import sys

def main():
    print("The file being opened's path is:", sys.argv[1])

    try:
        with open(sys.argv[1], 'r') as input_file:
            for line in input_file:
                current_line = line.strip()
                nums = current_line.split()
                if len(nums) != 2:
                    print("The current line does not have two float values")
                    continue
                else:
                    try:
                        num1 = float(nums[0])
                        num2 = float(nums[1])
                        print(f"{num1} + {num2} = {num1+num2}")
                    except ValueError:
                        print("The current line does not have two float values")

    except IOError:
        print("Please provide a valid file name")
        sys.exit()

main()