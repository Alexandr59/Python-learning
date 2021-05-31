import json
import os
from random import randint
import zipfile

# first script
input_data = []

for i in range(randint(1000, 10000)):
    input_data.append({
        "id": randint(0, 999999),
        "type": ['one', 'two', 'three', 'four', 'five'][randint(0, 4)]
    })

with open('input_data.json', 'w') as file:
    json.dump(input_data, file, indent=4)

# second script
one = []
two = []
three = []
four = []
five = []

with open('input_data.json', 'r') as file:
    data = json.load(file)

for element in data:
    if element["type"] == 'one':
        one.append(element)
    elif element["type"] == 'two':
        two.append(element)
    elif element["type"] == 'three':
        three.append(element)
    elif element["type"] == 'four':
        four.append(element)
    elif element["type"] == 'five':
        five.append(element)

with open('one.json', 'w') as file:
    json.dump(one, file, indent=4)
with open('two.json', 'w') as file:
    json.dump(two, file, indent=4)
with open('three.json', 'w') as file:
    json.dump(three, file, indent=4)
with open('four.json', 'w') as file:
    json.dump(four, file, indent=4)
with open('five.json', 'w') as file:
    json.dump(five, file, indent=4)

# extra
with zipfile.ZipFile('result.zip', 'w') as archive:
    archive.write('one.json')
    archive.write('two.json')
    archive.write('three.json')
    archive.write('four.json')
    archive.write('five.json')

os.remove('one.json')
os.remove('two.json')
os.remove('three.json')
os.remove('four.json')
os.remove('five.json')
