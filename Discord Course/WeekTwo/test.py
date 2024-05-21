def isLargest(num1, num2, num3):
    list = [num1, num2, num3]
    temp = 0
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j + 1] > list[i]:
                temp = list[i]       
                list[i] = list[j + 1]
                list[j + 1] = temp

    return list[0]

print(f'{isLargest(10, 4, 2)}')
