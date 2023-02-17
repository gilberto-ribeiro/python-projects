def minmax(list):
    largest = None
    smallest = None
    for i in list:
        if largest is None or largest < i:
            largest = i
        if smallest is None or smallest > i:
            smallest = i
    return [smallest, largest]


num = [3, 41, 12, 9, 74, 15]
print(minmax(num))