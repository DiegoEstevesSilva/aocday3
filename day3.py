import math

def get_prio (character):
    if character.islower():
        return ord(character) - 97 + 1 
    else:
        return ord(character) - 65 + 27

with open('day3 input.txt') as file:
    rucksacks = file.readlines()
    file.close()

prio_sum = 0


for rucksack in rucksacks:
    comp_size = math.floor(len(rucksack)/2)
    comp_1 = rucksack[:comp_size]
    comp_2 = rucksack[comp_size:].replace("\n","")

    for x in comp_1:
        if x in comp_2:
            prio_sum += get_prio(x)
            break

print(prio_sum)


