import random

wfiber_dict = {}
fiber_dict = {}
month_list = []

with open("raw.txt", "r") as raw:
    lines = raw.readlines()
    for line in lines:
        if line.strip() != "":
            line = line.replace("|", "").replace("\n", "").replace(",", "").split()
            head = " ".join(line[:-1])
            tail = line[-1]
            wfiber_dict[head] = float(tail)
        else:
            pass

for i in range(7):
    while sum(list(fiber_dict.values())) < 30:
        fiber_dict.update({random.choice(list(wfiber_dict.items()))})

    month_list.append(list(fiber_dict.items()))
    fiber_dict.clear()

for d, day in enumerate(month_list):  
    print(f"Day {d+1}: {str(day)[1:-1].replace("), (", " | ").replace("(", "").replace("'", "").replace(")", "")}", end='\n\n')