import numpy as np

number = int(input('Please enter your number: '))

results = []

while True:
    if number % 2 == 0:
        results.append(int(number/2))
        number = number/2
    elif number % 2 == 1:
        results.append(int((3*number) + 1))
        number = 3*number+1

    if 1 in results:
        break

print(results)
print('Max element: ',np.max(results))

