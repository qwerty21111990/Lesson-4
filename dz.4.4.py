arr1 = [1, 5, 6, 3, 5, 5, 7, 9, 1, 8, 3, 2, 3]
arr2 = []

for x in arr1:
    if arr1.count(x) > 2:
        arr2.append(x)

print(arr1)
print(arr2)
