atoms = int(input())
final_quantity = int(input())
time=0

while atoms>final_quantity:
    atoms /= 2
    time += 12
print(time)
