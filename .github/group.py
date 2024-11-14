# groups_of_3 function groups elements of a list into sublists with 3 elements each.

# Parameters:
# input_list: A list of integers that we want to group into sublists with 3 values

# Returns: A list of lists where each sublist contains a group of 3 consecutive values from the input list.
# If there are fewer than three values left in the input list at the end, the last sublist will contain the remaining values.
def groups_of_3(input_list: list[int]) -> list[list[int]]:
    output_list = []
    for i in range(0, len(input_list), 3):
        temp = []
        for j in range(i,min(i+3, len(input_list))):
            temp.append(input_list[j])
        output_list.append(temp)
    return output_list



