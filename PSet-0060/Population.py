Population_A = 50000000
Population_B = 70000000
year = 0
while (Population_A < Population_B):
    Population_A = Population_A + (Population_A * 3/100)
    Population_B = Population_B + (Population_B * 2/100)
    year = year + 1
print(year)
