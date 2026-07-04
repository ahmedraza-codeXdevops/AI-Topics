data = ["10", "20", "", "40", "abc", "50"]

clean = []

for item in data:
    if item.isdigit():
        clean.append(int(item))

print(clean)