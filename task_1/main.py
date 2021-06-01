with open('Sources for Task 1/happynumbers.txt', 'r') as file:
    happy_numbers = [int(n) for n in file]
with open('Sources for Task 1/primenumbers.txt', 'r') as file:
    prime_numbers = [int(n) for n in file]

total_numbers = []

for happy_number in happy_numbers:
    for prime_number in prime_numbers:
        if happy_number == prime_number:
            total_numbers.append(happy_number)

if total_numbers:
    print('Total number of files happynumbers.txt and primenumbers.txt')
    print(total_numbers)
else:
    print('No match found...')
