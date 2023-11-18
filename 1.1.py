
n = int(input())
temperature = float(input())
maximum = temperature
temperature = float(input())
if maximum < temperature:
    minimum = temperature
else:
    minimum = maximum
    maximum = temperature
for temperature in range(2, n + 1):
    temperature = float(input())
    if maximum < temperature:
        maximum = temperature
    if temperature < minimum:
        minimum = temperature
print(maximum - minimum)