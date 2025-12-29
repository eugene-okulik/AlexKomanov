def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


targets = {5, 200, 1000, 100000}
results = {}

for index, value in enumerate(fibonacci(), start=1):
    if index in targets:
        results[index] = value
        if len(results) == len(targets):
            break

print(results[5])
print(results[200])
print(results[1000])
print(results[100000])
