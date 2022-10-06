import itertools

numbers = list(range(20, 36))
cases = 0
total_cases = 0
for a in numbers:
    for b in numbers:
        for c in numbers:
            for d in numbers:
                total_cases += 1
                if a + b + c + d < 100:
                    cases += 1
probability = cases/total_cases
print('Combinations:', total_cases)
print('Desired combinations:', cases)
print('Probability:', probability)

cases2 = 0
total_cases2 = 0
for set in itertools.product(numbers, repeat=4):
    total_cases2 += 1
    if set[0] + set[1] + set[2] + set[3] < 100:
        cases2 += 1
print (cases2)
print (total_cases2)
print (cases2/total_cases2)

if cases == cases2 and total_cases == total_cases2:
    print('It works')