def groups_of_3(input_list: list[int]) -> list[list[int]]:
    output_list = []
    for i in range(0, len(input_list), 3):
        temp = []
        if i+2 <= input_list[i+2]:
            for j in range(i,i+3):
                temp.append(input_list[j])
        output_list.append(temp)
    return output_list



