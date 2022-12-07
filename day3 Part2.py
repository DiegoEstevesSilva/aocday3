import math

def get_prio (character):
    if character.islower():
        return ord(character) - 97 + 1 
    else:
        return ord(character) - 65 + 27

def split_in_groups(items: list[str]):
    group_items = []
    groups_list = []
    for idx, item in enumerate(items, start=1):
        group_items.append(item)
        if idx % 3 == 0:
            groups_list.append(group_items.copy())
            group_items.clear()
    return groups_list

def check_badge(items: list[str]):
    for x in items[0]:
        if (x in items[1]) and (x in items[2]):
            return x
        


with open('day3 input.txt') as file:
    elfs = file.readlines()
    file.close()


prio_sum = 0

elf_groups = split_in_groups(elfs)

for group in elf_groups:
    group_badge = check_badge(group)
    prio_sum += get_prio(group_badge)
    
print(prio_sum)

