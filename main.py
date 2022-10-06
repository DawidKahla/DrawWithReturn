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
