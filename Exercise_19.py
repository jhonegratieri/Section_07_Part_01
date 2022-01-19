vector = []

for i in range(50):
    vector.append((i + 5 * i) % (i + 1))

print(vector)