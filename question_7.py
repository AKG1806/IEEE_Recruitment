List_1 = [1, 2, 3, 4, 5, 6]
List_2 = [1, 3, 5, 7, 9]
Common = []
for num in List_2:
    if num in List_1:
        Common.append(num)

print("Common List", Common)