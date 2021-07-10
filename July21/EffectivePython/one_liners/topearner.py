employees = {
    'Alice': 100000,
    'Bob': 98000,
    'Cena': 127000,
    'Dwayne': 158000,
    'Frank': 88000
}

# find the top earner (every one with salary greater than or equal to 1 lakh)

top_earners = []
for name,salary in employees.items():
    if salary >= 100000:
        top_earners.append((name,salary))

print(top_earners)

## One-liner

top_earners = [(n,s) for n,s in employees.items() if s >= 100000 ]
print(top_earners)