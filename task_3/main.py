import json
import os
import datetime

with open('Sources for Task 3/categories.json', 'r') as file:
    categories = json.load(file)
with open('Sources for Task 3/locations.json', 'r') as file:
    locations = json.load(file)

opened = {}
for i in os.listdir('Sources for Task 3/opened'):
    with open(f'Sources for Task 3/opened/{i}', 'r') as file:
        opened[i[:-5]] = json.load(file)

updated = {}
for i in os.listdir('Sources for Task 3/updated'):
    with open(f'Sources for Task 3/updated/{i}', 'r') as file:
        updated[i[:-5]] = json.load(file)


def findCategory(tenant):
    for cat, ten in categories.items():
        for el in ten:
            if el == tenant:
                return cat
    return 'not found...'


def findAddress(tenant):
    for address, tenants in locations['addresses'].items():
        for ten in tenants:
            if ten == tenant:
                return address
    return 'not found...'


def findStreet(address):
    return ' '.join(address.split()[1:])


def findDistrict(address):
    for st, district in locations['streets'].items():
        if st == ' '.join(address.split()[1:]):
            return district
    return 'not found...'


# Which and where a category(s) was(were) opened for the first time before 1900
print('\tFirst tenants before 1900\n')
for street, dateTenants in opened.items():
    for date, tenants in dateTenants.items():
        if date != 'null' and datetime.date(*map(int, date.split('-'))).year < 1900:
            for t in tenants:
                a = findAddress(t)
                print(f'Category: {findCategory(t)},\nAddress: {a},\nDistrict: {findDistrict(a)},\n'
                      f'Tenant: {t},\nFoundation date: {date}\n')
                category = findCategory(t)

# Which and where a category(s) was(were) opened for the last time
print('\n\n\n\n\n\tLast tenants after 2015\n')
for street, dateTenants in opened.items():
    for date, tenants in dateTenants.items():
        if date != 'null' and datetime.date(*map(int, date.split('-'))).year > 2015:
            for t in tenants:
                a = findAddress(t)
                print(f'Category: {findCategory(t)},\nAddress: {a},\nDistrict: {findDistrict(a)},\n'
                      f'Tenant: {t},\nFoundation date: {date}\n')
                category = findCategory(t)

# Which street’s tenants are the most out of date (has the stalest updated dates)?
print('\n\n\n\n\n\tStreet’s tenants are the most out of date: ', end='')
dates = [datetime.date(*map(int, date.split('-'))) for date in updated.keys()]
dates.sort()
streetsStalestUpdated = set()
for date in dates[:10]:
    for tenant in updated[str(date)]:
        streetsStalestUpdated.add(' '.join(findAddress(tenant).split()[1:]))
for street in streetsStalestUpdated:
    print(street, end=', ')

# Which street’s tenants are the most up to date (has the freshest updated dates)?
print('\n\n\n\n\n\tStreet’s tenants are the most up to date: ', end='')
dates.sort(reverse=True)
streetsFreshestUpdated = set()
for date in dates[:10]:
    for tenant in updated[str(date)]:
        streetsFreshestUpdated.add(' '.join(findAddress(tenant).split()[1:]))
for street in streetsFreshestUpdated:
    print(street, end=', ')

# Category amount for each district
print('\n\n\n\n\n\tCategory amount for each district: ')
districtsCategories = {}
for district in locations['streets'].values():
    districtsCategories[district] = set()
for category, tenants in categories.items():
    for tenant in tenants:
        districtsCategories[findDistrict(findAddress(tenant))].add(findCategory(tenant))
for district, cat in districtsCategories.items():
    print(f'District: {district}, Category amount: {len(cat)}')

# Street leaderboard, list streets with the highest amount of specific category (for example “West Franklin Street - Restaurants – 25")
print('\n\n\n\n\n\tList streets with the highest amount of specific category: ')
dictStreetsCategoriesTenants = {}
for category in categories.keys():
    dictStreetsCategoriesTenants[category] = {}
    for street in locations['streets']:
        dictStreetsCategoriesTenants[category][street] = 0
for category, tenants in categories.items():
    for tenant in tenants:
        dictStreetsCategoriesTenants[category][findStreet(findAddress(tenant))] += 1

for category, streetsAndAmount in dictStreetsCategoriesTenants.items():
    highest = ''
    i = 0
    for street, amount in streetsAndAmount.items():
        if i < amount:
            i = amount
            highest = f'{street} - {category} - {amount}'
    if highest:
        print(highest)

# Street looser board, list streets with the lowest amount of specific category (for example “North Graham Street - Church – 1")
print('\n\n\n\n\n\tList streets with the lowest amount of specific category: ')
for category, streetsAndAmount in dictStreetsCategoriesTenants.items():
    highest = ''
    i = 100
    for street, amount in streetsAndAmount.items():
        if amount != 0 and i > amount:
            i = amount
            highest = f'{street} - {category} - {amount}'
    if highest:
        print(highest)
