#using lists
''' names = ["Lorna", "Stacey", "James"]

name = input("Name: ")

if name in names:
    print("Found")
else:
    print("Not Found")
'''

#using dictionaries
# Creating a list of dictionaries

'''
people = [
    {"name": "Lorna", "Number": "+254-721-098-630"},
    {"name": "Stacey", "Number": "+254-717-890-030"},
    {"name": "James", "Number": "+254-701-098-100"},
]


name = input("Name: ")

for person in people:
    if person["name"] == name:
        number = person["Number"]
        print(f"Found Number: {number}")
        break

else:
    print("Not Found")

'''

people = {
    "Lorna": "+254-721-098-630",
    "Stacey": "+254-717-890-030",
    "James": "+254-701-098-100"
}

name = input("Name: ")

if name in people:
    number = people[name]
    print(f"Found {number}")
else:
    print("Not Found")