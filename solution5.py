# find out 1000-3000 even number in list

result = []
for num in range(1000,3000):
    if num % 2 == 0:
        result.append(num)

print(result)