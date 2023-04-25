
names = []

for x in range(10):
    names.append(input("Enter Name: "))

for x in range(10):
    print(names.pop(0))

if len(names) == 0:
    print("[]")

print(names)
