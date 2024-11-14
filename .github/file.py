import sys

def main():
    if len(sys.argv) != 2:
        print("Please provide a valid file name")
        sys.exit()

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
